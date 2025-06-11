from qiskit import QuantumCircuit
 
def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    qc.h(range(n))
 
    return qc

from qiskit.quantum_info import Statevector

if __name__ == "__main__":
    qc = solve(3)
    print(Statevector(qc))