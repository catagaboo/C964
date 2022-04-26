# Package class creates package objects
class Package:
    def __init__(self, package_id, node_index, address, city, state, zip_code, delivery_deadline, weight, status):
        self.id = package_id
        self.node_index = node_index
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.delivery_time = 0
        self.departure_time = 0