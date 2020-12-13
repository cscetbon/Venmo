class Page(list):

    def __init__(self, method=None, user_id=None):
        super().__init__()
        self.method = method
        self.user_id = user_id

    def get_next_page(self):
        """
        Get the next page of transactions
        Note: As of now, it only works with get_user_transaction. Others will be added later.
        :return:
        """
        if not self.user_id or not self.method or len(self) < 1:
            return self.__init__()

        last_transaction = self[-1].id
        return self.method(user_id=self.user_id, before_id=last_transaction)
