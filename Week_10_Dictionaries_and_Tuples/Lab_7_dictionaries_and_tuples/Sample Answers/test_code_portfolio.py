from math import pi
import robot_sim   # your module containing detect_obstacles()


def run_test(name, robot_x, robot_y, sensor_angles, sensor_range, expected):
    print(f"Running {name} ... ", end="")

    result = robot_sim.detect_obstacles(
        robot_x,
        robot_y,
        sensor_angles,
        sensor_range,
        robot_sim.obstacles
    )

    if result == expected:
        print("PASS")
    else:
        print("FAIL")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")


def main():
    print("\n=== Testing detect_obstacles() ===\n")

    # -------------------------------------------------------------
    # 1. OBSTACLE DETECTION TESTS
    # -------------------------------------------------------------
    run_test(
        "Obstacle Test 1 — upward sensor hits obstacle 1",
        robot_x=2000,
        robot_y=1000,
        sensor_angles=[0],          # facing +Y
        sensor_range=500,
        expected=(True, "obstacle")
    )

    run_test(
        "Obstacle Test 2 — right sensor hits obstacle 3",
        robot_x=1400,
        robot_y=800,
        sensor_angles=[pi/2],       # facing +X
        sensor_range=300,
        expected=(True, "obstacle")
    )

    # -------------------------------------------------------------
    # 2. WALL DETECTION TESTS
    # -------------------------------------------------------------
    run_test(
        "Wall Test 1 — left sensor hits map_x_min = 0",
        robot_x=10,
        robot_y=2000,
        sensor_angles=[-pi/2],      # facing -X
        sensor_range=200,
        expected=(True, "wall")
    )

    run_test(
        "Wall Test 2 — downward sensor hits map_y_min = 0",
        robot_x=3000,
        robot_y=30,
        sensor_angles=[pi],         # facing -Y
        sensor_range=100,
        expected=(True, "wall")
    )

    # -------------------------------------------------------------
    # 3. NO COLLISION TESTS
    # -------------------------------------------------------------
    run_test(
        "Clear Test 1 — middle of map, no obstacles",
        robot_x=2500,
        robot_y=2500,
        sensor_angles=[-pi/4, 0, pi/4],
        sensor_range=200,
        expected=(False, None)
    )

    run_test(
        "Clear Test 2 — next to obstacle but facing away",
        robot_x=1400,
        robot_y=800,
        sensor_angles=[-pi/2],      # pointing away
        sensor_range=300,
        expected=(False, None)
    )

    # -------------------------------------------------------------
    # 4. MULTI-SENSOR TESTS
    # -------------------------------------------------------------
    run_test(
        "Multi-sensor Test — only right sensor detects obstacle",
        robot_x=1400,
        robot_y=800,
        sensor_angles=[-pi/2, 0, pi/2],
        sensor_range=300,
        expected=(True, "obstacle")
    )

    run_test(
        "Multi-sensor Clear Test — no sensor angle sees anything",
        robot_x=3000,
        robot_y=300,
        sensor_angles=[-pi/4, 0, pi/4],
        sensor_range=300,
        expected=(False, None)
    )

    print("\n=== Testing complete ===\n")


if __name__ == "__main__":
    main()
