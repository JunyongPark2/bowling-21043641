# Plan: Bowling Game Kata — Step 4

## 목표 (이번 단계에서 구현할 동작)

10번째 프레임 필볼(fill ball) 로직 — 단, 사전 확인 결과 현재 `score()` 구현(`range(10)`으로 프레임 수만 제한하고 롤 인덱스를 그대로 따라가는 방식)이 이미 아래 케이스들을 정확히 계산하고 있음을 확인했다:

- 퍼펙트 게임(12번 모두 스트라이크) → 300점
- 10번째 프레임 스페어 + 필볼 1개 → 정상 계산
- 10번째 프레임 스트라이크 + 필볼 2개 → 정상 계산

따라서 이번 단계는 새로운 프로덕션 코드 변경을 위한 RED가 아니라, **이미 만족되는 동작을 회귀 방지용 특성화(characterization) 테스트로 고정**하는 것이 목표다.

## 무엇을 테스트할 것인가

- `test_game.py`에 다음 3개 테스트 추가 (모두 코드 변경 없이 통과할 것으로 예상됨 — 특성화 테스트)

```python
def test_perfect_game_scores_300():
    game = Game()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300


def test_tenth_frame_spare_with_fill_ball():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert game.score() == 13


def test_tenth_frame_strike_with_two_fill_balls():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(10)
    game.roll(4)
    game.roll(5)
    assert game.score() == 19
```

## 검증 방식

- 통상적인 RED → GREEN이 아니라, 테스트 추가 직후 바로 `pytest` 실행해 **처음부터 통과**하는지 확인한다 (예상대로 통과하면 이는 실패가 아니라 "이미 충족된 동작을 문서화"하는 것임을 재확인하는 것).
- 프로덕션 코드(`game.py`) 변경 없음.

## 이번 단계에서 다루지 않는 것 (범위 제외)

- 입력값 검증
- 이 이후 다음 목표는 새로운 실제 동작(예: 여러 프레임 조합, 연속 스트라이크/스페어 혼합 게임 등 아직 다루지 않은 시나리오)을 찾아 진짜 RED가 발생하는 케이스로 진행한다.
