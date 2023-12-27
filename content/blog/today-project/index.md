# TODAY project

Not too long ago I decided to create a rather useless project. It shows emoji and color of the day. All of this is calculated by my formulas using my own algorithms on client-side.

Here are some formulas that I have used in TODAY project: 

* `t` - timestamp - const - 00:00 of this day in UTC.

### Emojis:
The formula incorporates certain coefficients that are already substituted. The formula is not fully adapted. Some Unicode characters are missing, so I tried to find the longest consecutive sequences of emojis.

* `tr` - `vector<int>` - const - the start of emoji sequences (in Unicode).
* `ts` - `vector<int>` - const - the difference between the numbers of the first and last elements in the sequences.
* `cet(t)` - a function used to calculate the sequence number of an emoji.
* `cev(t)` - a function used to calculate the decimal value of the emoji in Unicode.

$$cet(t) = \left\lfloor 23 \cdot \left(3 \sqrt[3]{t} + 0.7 \cdot \log(t + 5) \cdot 13 + \frac{t \bmod 86400}{86400} + 11 \cdot \log_2(t) + 17 \cdot \sin\left(\frac{2 \pi t}{86400}\right) + 2 \cdot \cos\left(\frac{2 \pi t}{86400}\right) + \left\lfloor \frac{t}{86400} \right\rfloor^2\right) \right\rfloor \bmod 4$$

$$cev(t) = tr[cet(t)] + \left\lfloor 17 * (3 \cdot sin(2 * pi * t / o.7) + 5 * (3 \sqrt[3]{t} + 13 \cdot \log(t + 11)) \right\rfloor \bmod cet(t)$$

and is output looks like `&#{cev(t)};`.

### Color:
Here, some cyclic operations are used, making it challenging to represent in a formulaic manner. I'll express it in pseudocode with a mix of mathematical formulas. This pseudocode may seem unconventional, but I am a genius, billionaire, and philanthropist. I have the complete right to use my algorithmic language if I am confident it will be understood by the reader (generally a mix of languages, but I believe it's quite evident).

* `sv(t)` - a function used to fill an array (not implemented as a function).
* `cf(n)` - a function used to precalculate factorial (not implemented as a function).
* `num2permutation(k, n)` - a function used to determine the required permutation (from $n!$) of the sequence corresponding to number k in lexicographical order.

```
func sv(int t) -> vector<int> {
  vector<int> el(3, 0);

  el[0] = t mod 1000;
  el[1] = ⌊(t mod 1000000 - el[0]) / 1000⌋;
  el[2] = ⌊(t - el[1] - el[0]) / 1000000⌋;

  return el;
}
```

```
func cf(int n) -> vector<int> {
  vector<int> factorials(n + 1, 1);
  for i from 2 to n + 1 {
    factorials.push(factorials[i - 1] * i);
  }

  return factorials;
}
```

```
func num2permutation(int k, int n) -> vector<string> {
  vector<string> permutation(n, "0");
  vector<bool> was(n+1, false);
  int cur_free, already_was;

  for i from 1 to n {
    already_was = ⌊k / factorials[n - i]⌋;
    k = k mod factorials[n - i];
    cur_free = 0;

    for j from 1 to n {
      if was[j] is false:
        cur_free += 1;

        if cur_free == already_was + 1:
          permutation[i - 1] = (el[j - 1] mod 256) -> string;
          was[j] = true;
    }
  }

  return permutation;
}
```

The color is output in the RGB format.

---

*p.s. I feel that the task of finding the required permutation can be solved with a lower asymptotic complexity (`color.js`). If you have ideas, please write to me about it.*

*p.s. [v2] I hate MathJax(((*
