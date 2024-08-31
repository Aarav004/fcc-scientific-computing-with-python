class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width **2 + self.height**2) **0.5

    def get_picture(self):
        if self.width >50 or self.height > 50:
            return "Too big for picture."
        
        else:
            lines= ""
            for i in range(self.height):
                lines+= "*" * self.width +"\n"
            return lines
    
    def get_amount_inside(self, other):
        return self.get_area()// other.get_area()

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"
    
    

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    
    def set_side(self, new_length):
        self.set_height(new_length)
        self.set_width(new_length)

    def set_width(self, new_length):
        super().set_width(new_length)
        super().set_height(new_length)
    
    def set_height(self, new_length):
        super().set_height(new_length)
        super().set_width(new_length)
        
    def __str__(self):
        return f"{self.__class__.__name__}(side={self.width})"
