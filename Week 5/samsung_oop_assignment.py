# Base Class
class SamsungPhone:
    def __init__(self, model, storage, camera_megapixels):
        self.model = model
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def show_specs(self):
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Camera: {self.camera_megapixels}MP")

    def take_picture(self):
        print(f"{self.model} takes a picture with {self.camera_megapixels}MP camera!")

# Child Class (Inheritance + adding new features)
class SamsungFold(SamsungPhone):
    def __init__(self, model, storage, camera_megapixels, foldable):
        super().__init__(model, storage, camera_megapixels)
        self.foldable = foldable

    def show_specs(self):
        super().show_specs()
        print(f"Foldable: {'Yes' if self.foldable else 'No'}")

    def fold(self):
        if self.foldable:
            print(f"{self.model} is now folded! 📱➡️📏")
        else:
            print(f"{self.model} is not a foldable phone.")

# Example usage
phone1 = SamsungPhone("Galaxy S23", 256, 108)
phone2 = SamsungFold("Galaxy Z Fold5", 512, 50, True)

phone1.show_specs()
phone1.take_picture()
print("------")
phone2.show_specs()
phone2.take_picture()
phone2.fold()
