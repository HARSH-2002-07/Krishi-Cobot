import rclpy
from rclpy.node import Node

class CommNode(Node):
    def __init__(self):
        super().__init__('comm_node')
        self.get_logger().info("FarmComm Node initialized. Handling UR5 ↔ eBot communication.")

    def coordinate(self):
        self.get_logger().info("eBot requests container... UR5 loading now.")
        self.get_logger().info("UR5 acknowledges: Container transferred.")

def main(args=None):
    rclpy.init(args=None)
    node = CommNode()
    node.coordinate()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
