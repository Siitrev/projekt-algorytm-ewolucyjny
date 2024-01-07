from core.template.template import Population, Person
import numpy as np


class Strategy:
    def best_selection(
        self, population: Population, amount: int, maximization=False
    ) -> list[Person]:
        sample = sorted(population.people, reverse=maximization, key=lambda person: person.value)[
            :amount
        ]
        return sample

    def tournament_selection(
        self,
        population: Population,
        tournaments: int,
        amount_of_contestants: int,
        maximization=False,
    ) -> list[Person]:
        sample = []
        for _ in range(tournaments):
            tournament = list(np.random.choice(population.people, amount_of_contestants, replace=False))
            print(tournament)
            if maximization:
                best_contestant = max(tournament, key=lambda person: person.value)
            else:
                best_contestant = min(tournament, key=lambda person: person.value)
            sample.append(best_contestant)
        return sample

    def roulette_wheel(self, population: Population, maximization=False) -> list[Person]:
        sum_of_fitness = sum([person.value for person in population.people])
        pass
