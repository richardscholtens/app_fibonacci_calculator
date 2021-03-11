# -*- coding: utf-8 -*-
"""Calculator views."""

from fibonacci_calculator.pure_python.fibonacci_calculator_pure import FibonacciSequenceService

from fibonacci_calculator.fibonacci_calculator import FibonacciSequenceService as FibonacciSequenceServiceCython



from flask import Blueprint, flash, render_template, request

from application_fibonacci_calculator.calculators.forms import FibonacciSequenceForm
from time import time

blueprint = Blueprint(
    "calculators", __name__, url_prefix="/calculators", static_folder="../static"
)


@blueprint.route("/retrieve_sequence/", methods=["GET", "POST"])
def retrieve_sequence():
    """Retrieve sequence page"""
    form_sequence = FibonacciSequenceForm()
    if request.method == "POST":
        if isinstance(form_sequence.number.data, int):
            start1 = time()
            fib_num = FibonacciSequenceService()
            fib_num.increase_sequence_length(form_sequence.number.data)
            sequence = fib_num.get_sequence()
            end1 = time() - start1

            start2 = time()
            fib_num_cython = FibonacciSequenceServiceCython()
            fib_num_cython.increase_sequence_length(form_sequence.number.data)
            sequence_cython = fib_num_cython.get_sequence()
            end2 = time() - start2

            times_faster = round((end1 / end2 * 100), 2)

            flash("You have succesfully retrieved the Fibonacci Sequence.", "success")
            return render_template(
                "calculators/retrieve_sequence.html",
                sequence=sequence,
                sequence_cython=sequence_cython,
                form_sequence=form_sequence,
                end1=end1,
                end2=end2,
                times_faster=times_faster,
            )
        else:
            flash(
                "You have failed to retrieve the Fibonacci Sequence. "
                "Please give a number as input.",
                "danger",
            )
        return render_template(
            "calculators/retrieve_sequence.html", form_sequence=form_sequence
        )
    return render_template(
        "calculators/retrieve_sequence.html", form_sequence=form_sequence
    )


@blueprint.route("/retrieve_number/", methods=["GET", "POST"])
def retrieve_number():
    """Retrieve number page"""
    form_number = FibonacciSequenceForm()
    if request.method == "POST":
        start1 = time()
        fib_num = FibonacciSequenceService()
        fib_num.increase_sequence_length(form_number.number.data)
        number = fib_num.get_nth(form_number.number.data)
        end1 = time() - start1

        start2 = time()
        fib_num_cython = FibonacciSequenceServiceCython()
        fib_num_cython.increase_sequence_length(form_number.number.data)
        number_cython = fib_num_cython.get_nth(form_number.number.data)
        end2 = time() - start2

        times_faster = round((end1 / end2 * 100), 2)


        if number:
            flash("You have succesfully retrieved the Fibonacci Number.", "success")
        else:
            flash(
                "You have failed to retrieve a Fibonacci Number. "
                "Please give an index number as input.",
                "danger",
            )
        return render_template("calculators/retrieve_number.html",
                               number=number,
                               number_cython=number_cython,
                               form_number=form_number,
                               end1=end1,
                               end2=end2,
                               times_faster=times_faster,
                               )
    return render_template("calculators/retrieve_number.html", form_number=form_number)


@blueprint.route("/retrieve_index/", methods=["GET", "POST"])
def retrieve_index():
    """Retrieve closest page"""
    form_index = FibonacciSequenceForm()
    if request.method == "POST":
        start1 = time()
        fib_num = FibonacciSequenceService()
        index = fib_num.get_sequence_index(form_index.number.data)
        end1 = time() - start1

        start2 = time()
        fib_num_cython = FibonacciSequenceServiceCython()
        index_cython = fib_num_cython.get_sequence_index(form_index.number.data)
        end2 = time() - start2

        times_faster = round((end1 / end2 * 100), 2)

        if index:
            flash("You have succesfully retrieved the Fibonacci Index.", "success")
        else:
            flash(
                "You have failed to retrieve the Fibonacci Index. "
                "Please give a number as input",
                "danger",
            )
        return render_template("calculators/retrieve_index.html",
                               index=index,
                               index_cython=index_cython,
                               form_index=form_index,
                               end1=end1,
                               end2=end2,
                               times_faster=times_faster,
                               )
    return render_template("calculators/retrieve_index.html", form_index=form_index)
