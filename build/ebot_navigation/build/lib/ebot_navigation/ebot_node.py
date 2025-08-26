import rclpy
from rclpy.node import Node

class EBotNode(Node):
    def __init__(self):
        super().__init__('ebot_node')
        self.get_logger().info("eBot initialized. Starting farm patrol...")
        # Future: SLAM + LiDAR + spraying system

    def patrol(self):
        self.get_logger().info("Navigating row 1... Triangle detected → Spraying fertilizer.")
        self.get_logger().info("Square detected → Logging issue.")

def main(args=None):
    rclpy.init(args=args)
    node = EBotNode()
    node.patrol()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
