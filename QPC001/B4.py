from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import XGate
import math


def add_negative_gate(
    qc: QuantumCircuit, n: int, zero_indices: list[int], t: QuantumRegister, base: int
):
    if len(zero_indices) > 0:
        qc.x(zero_indices)
    qc.append(XGate().control(n - base), [*range(base, n), t])
    qc.crx(math.pi * 2.0, t, 0)
    # Restore the state of t
    qc.append(XGate().control(n - base), [*range(base, n), t])
    if len(zero_indices) > 0:
        qc.x(zero_indices)


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:

    # FOR TEST
    qc.h(range(n))

    t = QuantumRegister(1, "t")
    qc.add_bits(t)

    bits = [((L - 1) >> j) & 1 for j in range(n)]

    for i in reversed(range(n)):
        if bits[i] == 1:
            zero_indices = [
                j + i for j, bit in enumerate([0] + bits[i + 1 :]) if bit == 0
            ]
            add_negative_gate(qc, n, zero_indices, t, i)

    # Add gate for L-1
    zero_indices = [j for j, bit in enumerate(bits) if bit == 0]
    add_negative_gate(qc, n, zero_indices, t, 0)

    return qc


from qiskit.quantum_info import Statevector

if __name__ == "__main__":
    qc = solve(4, 10)

    sv = Statevector(qc)
    print(sv)
    # ビットの出力は、 [t, qn, qn-1, ..., q0] となる
    for bits, prob in sv.probabilities_dict().items():
        print(f"{bits}: {prob:.4f}")
    print(qc.draw())
