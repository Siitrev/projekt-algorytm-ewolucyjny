from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QMainWindow,
    QLineEdit,
    QVBoxLayout,
    QComboBox,
    QCheckBox,
    QLabel
)



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Genetic algorithm [name of a function]")
        self.setFixedHeight(600)
        self.setFixedWidth(350)

        layout = QVBoxLayout()
        # Set table properties
        begin_txt = QLineEdit(placeholderText="Begin of the range - a")
        end_txt = QLineEdit(placeholderText="End of the range - b")
        population_amount_txt = QLineEdit(placeholderText="Population amount")
        precision_txt = QLineEdit(placeholderText="Precision")
        chromosome_amount_txt = QLineEdit(placeholderText="Best and tournament chromosome amount")
        elite_strategy_amount_txt = QLineEdit(placeholderText="Elite strategy amount")
        crossing_probability_txt = QLineEdit(placeholderText="Crossing probability")
        mutation_probability_txt = QLineEdit(placeholderText="Mutation probability")
        inversion_probability_txt = QLineEdit(placeholderText="Inversion probability")
        selection_method_label = QLabel("Selection method:")
        selection_method_combo = QComboBox()
        crossing_method_label = QLabel("Crossing method:")
        crossing_method_combo = QComboBox()
        mutation_method_label = QLabel("Mutation method:")
        mutation_method_combo = QComboBox()
        maximization_checkbox = QCheckBox("Maximization")
        btn_confirm = QPushButton("Confirm")

        layout.addWidget(begin_txt)
        layout.addWidget(end_txt)
        layout.addWidget(population_amount_txt)
        layout.addWidget(precision_txt)
        layout.addWidget(chromosome_amount_txt)
        layout.addWidget(elite_strategy_amount_txt)
        layout.addWidget(crossing_probability_txt)
        layout.addWidget(mutation_probability_txt)
        layout.addWidget(inversion_probability_txt)
        layout.addWidget(selection_method_label)
        layout.addWidget(selection_method_combo)
        layout.addWidget(crossing_method_label)
        layout.addWidget(crossing_method_combo)
        layout.addWidget(mutation_method_label)
        layout.addWidget(mutation_method_combo)
        layout.addWidget(maximization_checkbox)
        layout.addWidget(btn_confirm)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)