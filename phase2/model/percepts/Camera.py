class Camera :

    range_camera = 100
    width_camera = 20

    def __init__(self,robotAgent) -> None:
        self.robotAgent = robotAgent

    def getPercept() :
        return []

    def getRobotAgent(self) :
        return self.robotAgent


    def get_relative_Y(self,max_height) -> float:
        """
        Retourne la valeur y relative
        """
        return (self.robotAgent.getY() + self.robotAgent.getHeight()) / max_height

    def get_relative_X(self,max_width) -> float:
        """
        Retourne la valeur x relative
        """
        return ( ( self.robotAgent.getX() + (self.robotAgent.getWidth() / 2) )  - (Camera.width_camera/2)) / max_width

    def get_relative_height(self,max_height) -> float:
        """
        Retourne la hauteur relative
        """
        return Camera.range_camera / max_height

    def get_relative_width(self,max_width) -> float:
        """
        Retourne la largeur relative
        """
        return Camera.width_camera / max_width
    
    def getX(self) -> float :
        return self.robotAgent.getX()
    
    def getY(self) -> float :
        return self.robotAgent.getY()
    
    def getHeight(self) -> float :
        return self.range_camera
    
    def getWidth(self) -> float :
        return self.width_camera