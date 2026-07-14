# Plan: Bowling Game Kata — Step 1

## 목표 (이번 단계에서 구현할 동작)

가장 단순한 케이스부터 시작한다: **모든 프레임이 거터(gutter)인 게임의 점수는 0이다.**

이 테스트를 통과시키는 데 필요한 최소한의 `Game` 클래스와 `roll`/`score` 인터페이스만 만든다.

## 무엇을 테스트할 것인가

- `test_game.py`에 `test_gutter_game_scores_zero` 테스트 작성
- `Game` 인스턴스를 만들고, 20번 `roll(0)`을 호출한 뒤 `score()`가 `0`을 반환하는지 확인

```python
from game import Game

def test_gutter_game_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0
```

## 왜 이 테스트부터인가

- 프레임/스트라이크/스페어 등 복잡한 규칙 없이, `Game` 클래스의 기본 골격(`roll`, `score`, 롤 기록 저장)을 세울 수 있는 가장 단순한 케이스
- 이후 단계(스페어, 스트라이크, 퍼펙트 게임, 10번째 프레임 필볼)로 점진적으로 확장할 기반이 됨

## 어떻게 구현할 것인가 (GREEN 단계 예상 — 최소 구현)

- `game.py`에 `Game` 클래스 생성
- `roll(pins)`: 굴린 핀 수를 내부 리스트에 저장
- `score()`: 저장된 롤들의 합을 반환 (아직 스페어/스트라이크 보너스 로직 없음 — 이번 테스트는 그것을 요구하지 않음)

## 이번 단계에서 다루지 않는 것 (범위 제외)

- 스페어/스트라이크 보너스 계산
- 10번째 프레임 필볼 로직
- 입력값 검증

이 항목들은 이후 단계에서 각각 별도의 Plan.md로 진행합니다.
