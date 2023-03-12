class Vendas():
    def __init__(self) -> None:
        self.vendas = []

    def get(self) -> None:
        return self.__dict__

    def getOne(self, id: int) -> None:
        for index, venda in enumerate(self.vendas):
            if index == id:
                return venda
        return None

    def post(self, description: str, paymentType: int, value: float) -> None:
        self.vendas.append({
            'id': int(len(self.vendas)+1),
            'description': description,
            'paymentType': paymentType,
            'value': value
        })
        return self.__dict__

    def put(self, id: int, description: str, paymentType: int, value: float) -> None:
        for index, venda in enumerate(self.vendas):
            if index == id:
                venda['description'] = description
                venda['paymentType'] = paymentType
                venda['value'] = value
                return self.__dict__
        return None

    def delete(self, id: int) -> None:
        for index, venda in enumerate(self.vendas):
            if index == id:
                self.vendas.pop(index)
                return self.__dict__
        return None