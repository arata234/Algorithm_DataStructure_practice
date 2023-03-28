from enigma import PlugBoard, Rotor, Reflector, ALPHABET

if __name__ == "__main__":
    map_alphabet = {}
    plug_board = PlugBoard("BADC")
    rotor = Rotor("BADC", 1)
    
    rotor.rotate()
    