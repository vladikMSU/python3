class Overall:
    num_clicks=0

    @classmethod
    def click(cls):
        cls.num_clicks += 1
        return cls.num_clicks