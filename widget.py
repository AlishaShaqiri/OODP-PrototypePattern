import copy


class Widget:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)


class WidgetFactory:
    def __init__(self):
        self.widgets = {}

    def register_widget(self, name, widget):
        self.widgets[name] = widget

    def create_widget(self, name):
        if name in self.widgets:
            return self.widgets[name].clone()
        else:
            raise ValueError(f"Widget '{name}' not registered.")


if __name__ == "__main__":
    widget_factory = WidgetFactory()
    widget_factory.register_widget("TextWidget", Widget("TextWidget"))
    widget_factory.register_widget("GraphWidget", Widget("GraphWidget"))

    widget1 = widget_factory.create_widget("TextWidget")
    widget2 = widget_factory.create_widget("GraphWidget")
    widget3 = widget_factory.create_widget("TextWidget")

    print(widget1.name)  # Output: TextWidget
    print(widget2.name)  # Output: GraphWidget
    print(widget3.name)  # Output: TextWidget
