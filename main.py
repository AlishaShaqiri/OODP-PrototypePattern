from widget import  Widget, WidgetFactory

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
