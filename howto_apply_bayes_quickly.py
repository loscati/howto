"""Reference: https://youtu.be/HZGCoVF3YvM"""


class probability:
    def __init__(self, prior) -> None:
        self.prob = prior
        self.odds = self.to_odds(prior)

    def to_odds(self, p) -> float:
        return p / (1 - p)

    def to_prob(self, o) -> float:
        return o / (1 + o)

    def update(self, test) -> None:
        posterior_odds = test.b_factor * self.odds
        self.odds = posterior_odds
        self.prob = self.to_prob(posterior_odds)


class test:
    def __init__(self, sensitivity, specificity) -> None:
        self.b_factor = self.bayes_factor(sensitivity, specificity)

    def bayes_factor(self, sensitivity, specificity) -> float:
        # false positive rate
        fpr = 1 - specificity
        return sensitivity / fpr


if __name__ == "__main__":
    T = test(0.98, 0.98)
    prevalence = 0.017  # COVID-19, Jan 22-30 Italy
    prevalence = 0.2  # prob to be infected after 9 days
    PSp = probability(prevalence)  # prob to be sick if the test gives a positive result
    PSp.update(T)
    print(PSp.prob)
