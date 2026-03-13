# 리스트와 딕셔너리 (파이썬 기본 자료구조)

## 개요

파이썬의 기본 자료구조인 **리스트(list)**와 **딕셔너리(dict)**를 활용하여 데이터를 다루는 기초를 학습합니다.

## 리스트 (List)

- 순서가 있는 가변 시퀀스
- 인덱스로 접근: `lst[0]`, `lst[-1]`
- 자주 쓰는 메서드: `append()`, `extend()`, `pop()`, `sort()`

## 딕셔너리 (Dict)

- Key-Value 쌍 저장
- 조회: `d[key]` → Key 없으면 `KeyError`, `d.get(key, default)` → 없으면 `default` 반환
- `key in d`로 존재 여부 확인 (조회 전 체크에 활용)
- Value는 점수·설정 등과 같은 데이터 저장에 활용

## 리스트 컴프리헨션

```python
scores = [student['score'] for student in students]
above_average = [s['name'] for s in students if s['score'] >= average]
```

## 활용 예시

- 학생 점수 리스트에서 평균 계산: `sum(scores) / len(scores)`
- 조건에 맞는 요소 추출: 반복문 또는 리스트 컴프리헨션

## 주의사항

- 빈 리스트(`students == []`)일 때: `len(students)`가 0이 되어 0으로 나누기 가능 → 사전에 `if not students: return 0, []` 등으로 처리

## 관련 코드

`week2/basic/01_python_dict.py`
