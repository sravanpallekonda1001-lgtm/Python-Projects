class Car:
    def __init__(self, brand, model, color, eng_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.eng_type = eng_type

    def details(self):
        print("Car name is:", self.brand)
        print("Model name is:", self.model)
        print("Color name is:", self.color)
        print("Engine type is:", self.eng_type)

    def change_eng_type(self, new_type=None):
        if new_type:
            self.eng_type = new_type
            print("Successfully updated engine type to:", self.eng_type)
        else:
            ask = input("Do you want to change the engine type [Y|N]? ").strip().lower()
            if ask == "y":
                if self.eng_type.lower() == "diesel":
                    self.eng_type = "CNG"
                    print("Successfully updated engine type to:", self.eng_type)
                elif self.eng_type.lower() == "petrol":
                    print("This is a petrol type engine")
                else:
                    print("Unknown engine type")
            else:
                print("Thanks for coming")
