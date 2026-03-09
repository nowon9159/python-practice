```
    int_error = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

이런 ValueError 에러가 났고, abc는 10진수에 해당하지 않는다고 뜬다. int() 함수는 10진수 기반으로 숫자인지 아닌지 value를 판단하는 함수인듯?