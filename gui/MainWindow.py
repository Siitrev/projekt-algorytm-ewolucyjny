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
        self.begin_txt = QLineEdit(placeholderText="Begin of the range - a")
        self.end_txt = QLineEdit(placeholderText="End of the range - b")
        
        self.population_amount_txt = QLineEdit(placeholderText="Population amount")
        self.precision_txt = QLineEdit(placeholderText="Precision")
        self.chromosome_amount_txt = QLineEdit(placeholderText="Selection chromosome amount")
        self.elite_strategy_amount_txt = QLineEdit(placeholderText="Elite strategy amount")
        self.crossing_probability_txt = QLineEdit(placeholderText="Crossing probability")
        self.mutation_probability_txt = QLineEdit(placeholderText="Mutation probability")
        self.inversion_probability_txt = QLineEdit(placeholderText="Inversion probability")
        
        self.amount_of_contestanst_txt = QLineEdit(placeholderText="Amount of contestants")
        self.amount_of_contestanst_txt.setVisible(0)
        
        selection_method_label = QLabel("Selection method:")
        self.selection_method_combo = QComboBox()
        self.selection_method_combo.currentIndexChanged.connect(self.show_details)
        self.selection_method_combo.addItem("BEST")
        self.selection_method_combo.addItem("TOURNAMENT")
        self.selection_method_combo.addItem("ROULETTE")
        
        crossing_method_label = QLabel("Crossing method:")
        self.crossing_method_combo = QComboBox()
        
        mutation_method_label = QLabel("Mutation method:")
        self.mutation_method_combo = QComboBox()
        
        self.maximization_checkbox = QCheckBox("Maximization")
        
        btn_confirm = QPushButton("Confirm")

        layout.addWidget(self.begin_txt)
        layout.addWidget(self.end_txt)
        layout.addWidget(self.population_amount_txt)
        layout.addWidget(self.precision_txt)
        layout.addWidget(self.chromosome_amount_txt)
        layout.addWidget(self.elite_strategy_amount_txt)
        layout.addWidget(self.crossing_probability_txt)
        layout.addWidget(self.mutation_probability_txt)
        layout.addWidget(self.inversion_probability_txt)
        layout.addWidget(selection_method_label)
        layout.addWidget(self.selection_method_combo)
        layout.addWidget(self.amount_of_contestanst_txt)
        layout.addWidget(crossing_method_label)
        layout.addWidget(self.crossing_method_combo)
        layout.addWidget(mutation_method_label)
        layout.addWidget(self.mutation_method_combo)
        layout.addWidget(self.maximization_checkbox)
        layout.addWidget(btn_confirm)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def show_details(self, ind : int):
        self.amount_of_contestanst_txt.setVisible(0)
        if ind == 1:
            self.amount_of_contestanst_txt.setVisible(1)