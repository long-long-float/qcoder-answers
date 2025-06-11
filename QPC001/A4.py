from qiskit import QuantumCircuit
 
 
def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.h(0)
    qc.ch(0, 1)
    qc.cx(1, 0)
 
    return qc

from qiskit.quantum_info import Statevector

if __name__ == "__main__":
    qc = solve()
    print(Statevector(qc))