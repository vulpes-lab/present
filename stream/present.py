import random
import hashlib


class Present:
    """プレゼント企画の抽選用クラス"""

    def __init__(self, supporters: tuple, seed: str):
        # 応募者
        self.supporters = supporters

        # シード値の設定
        random.seed(
            hashlib.sha1(seed.encode()).hexdigest()
        )

    def lottery(self):
        """抽選結果を返す"""

        # 人数
        num = int(len(self.supporters)) - 1

        # 範囲内でランダムに抽選する
        rand_index = random.randrange(0, num)

        return self.supporters[rand_index]
