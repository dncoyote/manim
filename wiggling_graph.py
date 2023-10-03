from manim import *
import networkx as nx


class WigglingGraph(Scene):
    def graph_configure(self, graph, **kwargs):
        for submob in graph.vertices.values():
            submob.jiggling_direction = rotate_vector(
                RIGHT, np.random.random() * TAU * 1.5
            )
            submob.jiggling_phase = np.random.random() * TAU * 1.5

        for key, value in kwargs.items():
            setattr(graph, key, value)

    def set_graph_stroke(self, graph, **kwargs):
        for e in graph.edges.values():
            e.set_stroke(**kwargs)

    def construct(self):
        # Create a white background rectangle covering the entire frame
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=0,
        )
        self.add(background)

        def wiggle_graph_updater(graph, dt):
            for key in graph.edges:
                edge = graph.edges[key]
                edge.start = graph.vertices[key[0]].get_center()
                edge.end = graph.vertices[key[1]].get_center()

            for submob in graph.vertices.values():
                submob.jiggling_phase += dt * graph.jiggles_per_second * TAU
                submob.shift(
                    graph.jiggle_amplitude *
                    submob.jiggling_direction *
                    np.sin(submob.jiggling_phase) * dt
                )

        graph = nx.newman_watts_strogatz_graph(50, 6, 0.1, seed=248)
        graph_mob = Graph.from_networkx(
            graph, layout="kamada_kawai", layout_scale=4, labels=False)

        # Set node colors
        for node in graph_mob.vertices.values():
            if np.random.random() > 0.5:
                node.set_fill(YELLOW)
            else:
                node.set_fill(RED)

        self.graph_configure(
            graph_mob, jiggle_amplitude=0.3, jiggles_per_second=0.3)

        # Set the stroke color of edges to black
        self.set_graph_stroke(graph_mob, color=BLACK, width=0.35)

        graph_mob.add_updater(wiggle_graph_updater)
        self.add(graph_mob)
        # with register_font("BebasNeue-Regular.ttf"):
        #     text = Text("Hi! I am Bilal.", font_size=72,
        #                 font="BebasNeue-Regular", color=BLACK)
        text = Text("Hi! I am Bilal.", color=BLACK)
        text.move_to(ORIGIN)
        self.wait(3)
        self.play(AddTextLetterByLetter(text))
        self.wait(3)
        self.play(RemoveTextLetterByLetter(text))
        self.wait(3)
