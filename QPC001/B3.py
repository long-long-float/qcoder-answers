from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import XGate
import math


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:

    # FOR TEST
    # qc.h(range(n))

    t = QuantumRegister(1, "t")
    qc.add_bits(t)

    for i in range(L):
        # i to binary bits
        bits = [(i >> j) & 1 for j in range(n)]

        # Apply gates based on bits
        zero_indices = [j for j, bit in enumerate(bits) if bit == 0]
        if len(zero_indices) > 0:
            qc.x(zero_indices)
        qc.append(XGate().control(n), [*range(n), t[0]])
        qc.crx(math.pi * 2.0, t, 0)
        # Restore the state of t
        qc.append(XGate().control(n), [*range(n), t[0]])
        if len(zero_indices) > 0:
            qc.x(zero_indices)

    return qc


from qiskit.quantum_info import Statevector

if __name__ == "__main__":
    qc = solve(3, 2**3)

    sv = Statevector(qc)
    print(sv)
    # ビットの出力は、 [t, qn, qn-1, ..., q0] となる
    for bits, prob in sv.probabilities_dict().items():
        print(f"{bits}: {prob:.4f}")
    print(qc.draw())
