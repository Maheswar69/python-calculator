{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyNHlOzkjxEcXk9OLcmCWfPb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Maheswar69/python-calculator/blob/main/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PDRnE-s9xTVn",
        "outputId": "72ed1c99-f6f6-40cd-f2b4-7a55efbcb0d9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Add:  15\n",
            "Subtract:  5\n",
            "Multiply:  50\n",
            "Divide:  2.0\n"
          ]
        }
      ],
      "source": [
        "class Calculator:\n",
        "    def add(self, a, b):\n",
        "        return a + b\n",
        "\n",
        "    def subtract(self, a, b):\n",
        "        return a - b\n",
        "\n",
        "    def multiply(self, a, b):\n",
        "        return a * b\n",
        "\n",
        "    def divide(self, a, b):\n",
        "        if b != 0:\n",
        "            return a / b\n",
        "        else:\n",
        "            return \"Cannot divide by zero\"\n",
        "\n",
        "# Create an object and test it\n",
        "calc = Calculator()\n",
        "print(\"Add: \", calc.add(10, 5))\n",
        "print(\"Subtract: \", calc.subtract(10, 5))\n",
        "print(\"Multiply: \", calc.multiply(10, 5))\n",
        "print(\"Divide: \", calc.divide(10, 5))"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Ajrex4Bny39b"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}