import sys
sys.path.append('../../../../configs')
import test_boards

def get_board(type, name):
    power_ports = test_boards.test_boards[type]["power_ports"]
    for power_port in power_ports:
        for board in power_ports[power_port]:
            if board == name:
                return power_ports[power_port][board]

    return None
