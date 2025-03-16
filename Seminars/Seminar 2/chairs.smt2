; Declare integer variables for positions
(declare-const A Int) ; Alice
(declare-const B Int) ; Bob
(declare-const C Int) ; Charlie

; Each person must be in a distinct chair (0, 1, 2)
(assert (distinct A B C))

; Alice does not sit next to Charlie (|A - C| ≠ 1)
(assert (not (= (abs (- A C)) 1)))

; Alice does not sit on the leftmost chair (A ≠ 0)
(assert (not (= A 0)))

; Bob does not sit to the right of Charlie (B ≤ C)
(assert (<= B C))

; Valid chair positions (0, 1, 2)
(assert (and (>= A 0) (<= A 2)))
(assert (and (>= B 0) (<= B 2)))
(assert (and (>= C 0) (<= C 2)))

; Check satisfiability
(check-sat)
