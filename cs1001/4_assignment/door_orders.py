import random

##
# Class for describing an order of doors
# also includes tests for said class
##

class DoorOrder():
    
    # Total number of orders
    NoOfOrders = 0
    
    # number used in part of the next order ID
    NextOrderID = 500
    
    def __init__(self, quantity=0, height=198.1, width=76.2, depth=3.5, material='Wood'):
        DoorOrder.NoOfOrders += 1    
        
        # Sets instance vairables passed to object
        self.__quantity = quantity
        self. __height = height
        self.__width = width
        self.__depth = depth
        self.__material = material
        
        # Creates order ID and increments NextOrderID
        self.__orderID = f'{DoorOrder.NextOrderID}{random.randint(0, 9)}'
        DoorOrder.NextOrderID += 1
    
    def getOrderID(self):
        return self.__orderID
    
    def getHeight(self):
        return self.__height
    
    def getQuantity(self):
        return self.__quantity
    
    def setHeight(self, height):
        self.__height = height
    
    def setWidth(self, width):
        self.__width = width
    
    def setDepth(self, depth):
        self.__depth = depth

    def setQuantity(self, quantity):
        self.__quantity = quantity
    
    # Returns total surface area of all doors as int
    def getTotalSurfaceArea(self):
        return (
            (self.__height * self.__width * 2)+ # Front and back area
            (self.__depth * self.__height * 2)+ # Left and Right area
            (self.__depth * self.__width * 2) # Top and bottom area
        )*self.getQuantity() # Multiply the area of one door by the number of doors
        
    # Gets total cost of the order
    def getTotalCost(self):
        # Cost of base doors
        cost = self.getTotalSurfaceArea()*0.03
        
        # Adds extra cost based on material
        if self.__material == 'Fiberglass': cost *= 1.5
        if self.__material == 'Steel': cost *= 2

        return cost

    def __str__(self):
        # Formats surface area and total cost
        surfaceArea = '%.2f' % self.getTotalSurfaceArea()
        totalCost = '%.2f' % self.getTotalCost()

        return (
            f'Order ID: {self.getOrderID()}\n'
            f'Quantity Ordered: {self.getQuantity()} doors\n'
            f'Door Height: {self.getHeight()} cm\n'
            f'Door Width: {self.__width} cm\n'
            f'Door Depth: {self.__depth} cm\n'
            f'Door Material: {self.__material}\n'
            f'Total Surface Area: {surfaceArea} sq.cm\n'
            f'Total Cost of the Order: ${totalCost}\n'
        )

def main():
    # Creates orders
    orderOne = DoorOrder(10, 100, 50, 2, 'Fiberglass')
    orderTwo = DoorOrder(7, material='Steel')
    
    print(orderOne)
    print(orderTwo)
    
    
    # Change values of the second order
    orderTwo.setHeight(200)
    print(f'The height of doors for Order ID {orderTwo.getOrderID()} has been changed to 200.00 cm.')
    
    orderTwo.setQuantity(8)
    print(f'The quantity of doors for Order ID {orderTwo.getOrderID()} has been changed to 8.')
    
    # Formats then prints new price of order two after changes
    orderTwoNewPrice = '%.2f' % orderTwo.getTotalCost()
    print(f'The new cost for Order ID {orderTwo.getOrderID()} is ${orderTwoNewPrice}.\n')

    print(f'The total number of orders received was {DoorOrder.NoOfOrders}.\n')
    
    # Formats then prints the cost of all doors in all orders
    costOfAllDoors = "%.2f" % (orderOne.getTotalCost() + orderTwo.getTotalCost())
    print(f'The total cost of all orders received was ${costOfAllDoors}.')

if __name__ == '__main__':
    main()