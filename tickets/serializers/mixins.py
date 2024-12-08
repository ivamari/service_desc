class ExtendedView:
    multi_serializer_class = {}

    def get_serializer_class(self):
        try:
            return self.multi_serializer_class[self.action]
        except KeyError:
            return super().get_serializer_class()
