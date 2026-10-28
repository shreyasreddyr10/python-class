{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9kdMvDwLBAyUH2OAbVlC9"
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
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZQskXFvg28bb",
        "outputId": "eab736b3-9305-4e46-b42a-ad769999c6e7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(0, 0), (5, 1)]\n",
            "after append : [(0, 0), (5, 1), (2, 3)]\n",
            "after insert : [(9, 9), (0, 0), (5, 1), (2, 3)]\n",
            "after remove : [(9, 9), (0, 0), (2, 3)]\n",
            "length: 3 | sorted: [(0, 0), (2, 3), (9, 9)]\n"
          ]
        }
      ],
      "source": [
        "route = [(0, 0), (5, 1)]\n",
        "print(route)\n",
        "route.append((2, 3))\n",
        "print(\"after append :\", route)\n",
        "route.insert(0, (9, 9))\n",
        "print(\"after insert :\", route)\n",
        "route.remove((5, 1))\n",
        "print(\"after remove :\", route)\n",
        "print(\"length:\", len(route), \"| sorted:\", sorted(route))"
      ]
    }
  ]
}