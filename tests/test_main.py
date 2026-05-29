**Pytest uchun test kod**
```python
import pytest

def test_kvadratlar():
    def kvadratlar(n):
        return [i**2 for i in range(1, n+1)]

    assert kvadratlar(1) == [1]
    assert kvadratlar(2) == [1, 4]
    assert kvadratlar(3) == [1, 4, 9]
    assert kvadratlar(5) == [1, 4, 9, 16, 25]
```

**Jest uchun test kod**
```javascript
describe('kvadratlar', () => {
    it('1 dan 1 gacha sonlarning kvadratlarini chiqarsin', () => {
        const result = kvadratlar(1);
        expect(result).toEqual([1]);
    });

    it('1 dan 2 gacha sonlarning kvadratlarini chiqarsin', () => {
        const result = kvadratlar(2);
        expect(result).toEqual([1, 4]);
    });

    it('1 dan 3 gacha sonlarning kvadratlarini chiqarsin', () => {
        const result = kvadratlar(3);
        expect(result).toEqual([1, 4, 9]);
    });

    it('1 dan 5 gacha sonlarning kvadratlarini chiqarsin', () => {
        const result = kvadratlar(5);
        expect(result).toEqual([1, 4, 9, 16, 25]);
    });
});

function kvadratlar(n) {
    return Array.from({length: n}, (_, i) => (i + 1) ** 2);
}
```
