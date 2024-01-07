from core.template.template import Population, Person
import numpy as np


class Strategy:
    def best_selection(
        self, population: Population, amount: int, descending=False
    ) -> list[Person]:
        sample = sorted(population.people, reverse=descending, key=lambda x: x.value)[
            :amount
        ]
        return sample

    def tournament_selection(
        self, population: Population, tournaments: int, descending=False
    ) -> list[Person]:
        pass
