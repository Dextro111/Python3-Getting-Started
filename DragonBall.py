class Saiyans():
    def __init__(self, name, special_move="Ki_Blasts"):
        """Initializing A Saiyans Name And Special Move."""
        self.name = name
        self.special_move = special_move
    
    def super_saiyan(self):
        """Showing A Super Saiyan Transformation"""
        print(self.name.title() + " Has Transformed To Super-Saiyan!" )

    def super_saiyan_God(self):
        """Showing Super Saiyan God Transformation"""
        print(self.name.title() + " Has Entered God Mode And " + self.special_move +" is The Special Move ")

    def super_saiyan_Blue(self):
        """Showing Super Saiyan Blue Transformation"""
        print(self.name.title() + " Is Now On Super Saiyan Blue")

saiyan_vegeta = Saiyans("Vegeta", "Final Flair")

saiyan_vegeta.super_saiyan_God()

saiyan_goku = Saiyans("Goku", "Kamehameha")
saiyan_goku.super_saiyan_Blue()