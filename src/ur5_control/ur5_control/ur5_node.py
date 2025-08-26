import rclpy
from rclpy.node import Node

class UR5Node(Node):
    def __init__(self):
        super().__init__('ur5_node')
        self.get_logger().info("UR5 Node initialized. Waiting for eBot...")
        # Future: Subscribe to camera feed, perform sorting, container handling

    def simulate_action(self):
        self.get_logger().info("Sorting produce... Container ready for transfer.")

def main(args=None):
    rclpy.init(args=args)
    node = UR5Node()
    node.simulate_action()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
