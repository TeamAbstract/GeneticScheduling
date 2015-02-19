
class Vessels:
    """!
    Class that stores list of vessels as a static variable
    """
    vessels = list()  # list for total number of vessels
    id = 0  # static variable used for unique id

    def __init__(self):
        pass

    @staticmethod
    def addVessel(size):
        Vessels.vessels.append(Vessel(size, Vessels.id))
        Vessels.id += 1
        Vessels.vessels.sort(key=lambda x: x.size)

    @staticmethod
    def getVesselNum():
        return len(Vessels.vessels)

    @staticmethod
    def getFit(size):
        """! get the smallest vessel index that will fit the size
        :param size: size of order in kegs
        :return: integer index of the vessel or list of vessel indexes
        """

        for vessel in Vessels.vessels:
            if size <= vessel.size:
                return vessel.id

        # if too large for any one vessel
        vesselList = []
        for vessel in reversed(Vessels.vessels):
            while size > vessel.size:  # while still room in vessel uses largest first
                vesselList.append(vessel.id)
                size -= vessel.size
        vesselList.append(Vessels.getFit(size))  # add remaining barrels
        return sorted(vesselList)


class Vessel():
    """! internal representation of a vessel
    """
    def __init__(self, size, id):
        self.size = size
        self.id = id

    def getSize(self):
        return self.size
