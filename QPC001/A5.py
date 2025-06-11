from qiskit import QuantumCircuit
import math
 
def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    theta = 4 * math.atan(math.sqrt(6) / (3.0 + math.sqrt(3)))

    qc.ry(theta, 0)
    qc.ch(0, 1)
    qc.cx(1, 0)
 
    return qc

from qiskit.quantum_info import Statevector

if __name__ == "__main__":
    qc = solve()
    print(Statevector(qc))