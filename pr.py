{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "execution_count": null,
      "metadata": {
        "id": "p24vqxjtynUb"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pd.set_option('display.max_columns',None)\n",
        "pd.set_option('display.max_rows',None)"
      ],
      "metadata": {
        "id": "1IC_LzVjzSHb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('/content/smartphone_cleaned_v5.csv')"
      ],
      "metadata": {
        "id": "kKypBuf-zKt5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uk8BqOct2kD5",
        "outputId": "dfa68ce1-dadd-4b62-8553-163900fb14f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(980, 25)"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 426
        },
        "id": "ERLV8pENzOv_",
        "outputId": "cf4f1345-46f8-4124-9301-686898a80fe6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  brand_name                      model  price  rating  has_5g  has_nfc  \\\n",
              "0    oneplus              OnePlus 11 5G  54999    89.0    True     True   \n",
              "1    oneplus  OnePlus Nord CE 2 Lite 5G  19989    81.0    True    False   \n",
              "2    samsung      Samsung Galaxy A14 5G  16499    75.0    True    False   \n",
              "3   motorola       Motorola Moto G62 5G  14999    81.0    True    False   \n",
              "4     realme         Realme 10 Pro Plus  24999    82.0    True    False   \n",
              "\n",
              "   has_ir_blaster processor_brand  num_cores  processor_speed  \\\n",
              "0           False      snapdragon        8.0              3.2   \n",
              "1           False      snapdragon        8.0              2.2   \n",
              "2           False          exynos        8.0              2.4   \n",
              "3           False      snapdragon        8.0              2.2   \n",
              "4           False       dimensity        8.0              2.6   \n",
              "\n",
              "   battery_capacity  fast_charging_available  fast_charging  ram_capacity  \\\n",
              "0            5000.0                        1          100.0          12.0   \n",
              "1            5000.0                        1           33.0           6.0   \n",
              "2            5000.0                        1           15.0           4.0   \n",
              "3            5000.0                        1            NaN           6.0   \n",
              "4            5000.0                        1           67.0           6.0   \n",
              "\n",
              "   internal_memory  screen_size  refresh_rate    resolution  num_rear_cameras  \\\n",
              "0            256.0         6.70           120  1440 x 3216                  3   \n",
              "1            128.0         6.59           120  1080 x 2412                  3   \n",
              "2             64.0         6.60            90  1080 x 2408                  3   \n",
              "3            128.0         6.55           120  1080 x 2400                  3   \n",
              "4            128.0         6.70           120  1080 x 2412                  3   \n",
              "\n",
              "   num_front_cameras       os  primary_camera_rear  primary_camera_front  \\\n",
              "0                1.0  android                 50.0                  16.0   \n",
              "1                1.0  android                 64.0                  16.0   \n",
              "2                1.0  android                 50.0                  13.0   \n",
              "3                1.0  android                 50.0                  16.0   \n",
              "4                1.0  android                108.0                  16.0   \n",
              "\n",
              "   extended_memory_available  extended_upto  \n",
              "0                          0            NaN  \n",
              "1                          1         1024.0  \n",
              "2                          1         1024.0  \n",
              "3                          1         1024.0  \n",
              "4                          0            NaN  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3b55b894-e9c4-4f24-9aad-9dbe5fb60f2b\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>brand_name</th>\n",
              "      <th>model</th>\n",
              "      <th>price</th>\n",
              "      <th>rating</th>\n",
              "      <th>has_5g</th>\n",
              "      <th>has_nfc</th>\n",
              "      <th>has_ir_blaster</th>\n",
              "      <th>processor_brand</th>\n",
              "      <th>num_cores</th>\n",
              "      <th>processor_speed</th>\n",
              "      <th>battery_capacity</th>\n",
              "      <th>fast_charging_available</th>\n",
              "      <th>fast_charging</th>\n",
              "      <th>ram_capacity</th>\n",
              "      <th>internal_memory</th>\n",
              "      <th>screen_size</th>\n",
              "      <th>refresh_rate</th>\n",
              "      <th>resolution</th>\n",
              "      <th>num_rear_cameras</th>\n",
              "      <th>num_front_cameras</th>\n",
              "      <th>os</th>\n",
              "      <th>primary_camera_rear</th>\n",
              "      <th>primary_camera_front</th>\n",
              "      <th>extended_memory_available</th>\n",
              "      <th>extended_upto</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>oneplus</td>\n",
              "      <td>OnePlus 11 5G</td>\n",
              "      <td>54999</td>\n",
              "      <td>89.0</td>\n",
              "      <td>True</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>snapdragon</td>\n",
              "      <td>8.0</td>\n",
              "      <td>3.2</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>100.0</td>\n",
              "      <td>12.0</td>\n",
              "      <td>256.0</td>\n",
              "      <td>6.70</td>\n",
              "      <td>120</td>\n",
              "      <td>1440 x 3216</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>50.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>oneplus</td>\n",
              "      <td>OnePlus Nord CE 2 Lite 5G</td>\n",
              "      <td>19989</td>\n",
              "      <td>81.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>snapdragon</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.2</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>33.0</td>\n",
              "      <td>6.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>6.59</td>\n",
              "      <td>120</td>\n",
              "      <td>1080 x 2412</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>64.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1024.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>samsung</td>\n",
              "      <td>Samsung Galaxy A14 5G</td>\n",
              "      <td>16499</td>\n",
              "      <td>75.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>exynos</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.4</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>15.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>64.0</td>\n",
              "      <td>6.60</td>\n",
              "      <td>90</td>\n",
              "      <td>1080 x 2408</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>50.0</td>\n",
              "      <td>13.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1024.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>motorola</td>\n",
              "      <td>Motorola Moto G62 5G</td>\n",
              "      <td>14999</td>\n",
              "      <td>81.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>snapdragon</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.2</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "      <td>6.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>6.55</td>\n",
              "      <td>120</td>\n",
              "      <td>1080 x 2400</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>50.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1024.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>realme</td>\n",
              "      <td>Realme 10 Pro Plus</td>\n",
              "      <td>24999</td>\n",
              "      <td>82.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>dimensity</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.6</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>67.0</td>\n",
              "      <td>6.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>6.70</td>\n",
              "      <td>120</td>\n",
              "      <td>1080 x 2412</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>108.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3b55b894-e9c4-4f24-9aad-9dbe5fb60f2b')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3b55b894-e9c4-4f24-9aad-9dbe5fb60f2b button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3b55b894-e9c4-4f24-9aad-9dbe5fb60f2b');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w77Aj-rfzQEz",
        "outputId": "4ea103b4-d925-48e1-d07b-eb2f46889158"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 980 entries, 0 to 979\n",
            "Data columns (total 25 columns):\n",
            " #   Column                     Non-Null Count  Dtype  \n",
            "---  ------                     --------------  -----  \n",
            " 0   brand_name                 980 non-null    object \n",
            " 1   model                      980 non-null    object \n",
            " 2   price                      980 non-null    int64  \n",
            " 3   rating                     879 non-null    float64\n",
            " 4   has_5g                     980 non-null    bool   \n",
            " 5   has_nfc                    980 non-null    bool   \n",
            " 6   has_ir_blaster             980 non-null    bool   \n",
            " 7   processor_brand            960 non-null    object \n",
            " 8   num_cores                  974 non-null    float64\n",
            " 9   processor_speed            938 non-null    float64\n",
            " 10  battery_capacity           969 non-null    float64\n",
            " 11  fast_charging_available    980 non-null    int64  \n",
            " 12  fast_charging              769 non-null    float64\n",
            " 13  ram_capacity               980 non-null    float64\n",
            " 14  internal_memory            980 non-null    float64\n",
            " 15  screen_size                980 non-null    float64\n",
            " 16  refresh_rate               980 non-null    int64  \n",
            " 17  resolution                 980 non-null    object \n",
            " 18  num_rear_cameras           980 non-null    int64  \n",
            " 19  num_front_cameras          976 non-null    float64\n",
            " 20  os                         966 non-null    object \n",
            " 21  primary_camera_rear        980 non-null    float64\n",
            " 22  primary_camera_front       975 non-null    float64\n",
            " 23  extended_memory_available  980 non-null    int64  \n",
            " 24  extended_upto              500 non-null    float64\n",
            "dtypes: bool(3), float64(12), int64(5), object(5)\n",
            "memory usage: 171.4+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ng3S-wyx3e1W",
        "outputId": "c9a02b63-284d-48bd-f479-34039d6d1c24"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "brand_name                     0\n",
              "model                          0\n",
              "price                          0\n",
              "rating                       101\n",
              "has_5g                         0\n",
              "has_nfc                        0\n",
              "has_ir_blaster                 0\n",
              "processor_brand               20\n",
              "num_cores                      6\n",
              "processor_speed               42\n",
              "battery_capacity              11\n",
              "fast_charging_available        0\n",
              "fast_charging                211\n",
              "ram_capacity                   0\n",
              "internal_memory                0\n",
              "screen_size                    0\n",
              "refresh_rate                   0\n",
              "resolution                     0\n",
              "num_rear_cameras               0\n",
              "num_front_cameras              4\n",
              "os                            14\n",
              "primary_camera_rear            0\n",
              "primary_camera_front           5\n",
              "extended_memory_available      0\n",
              "extended_upto                480\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 426
        },
        "id": "uzmkm20-4ZVJ",
        "outputId": "a9b14a4b-51b5-47fe-c86b-00e9dc627d72"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  brand_name                      model  price  rating  has_5g  has_nfc  \\\n",
              "0    oneplus              OnePlus 11 5G  54999    89.0    True     True   \n",
              "1    oneplus  OnePlus Nord CE 2 Lite 5G  19989    81.0    True    False   \n",
              "2    samsung      Samsung Galaxy A14 5G  16499    75.0    True    False   \n",
              "3   motorola       Motorola Moto G62 5G  14999    81.0    True    False   \n",
              "4     realme         Realme 10 Pro Plus  24999    82.0    True    False   \n",
              "\n",
              "   has_ir_blaster processor_brand  num_cores  processor_speed  \\\n",
              "0           False      snapdragon        8.0              3.2   \n",
              "1           False      snapdragon        8.0              2.2   \n",
              "2           False          exynos        8.0              2.4   \n",
              "3           False      snapdragon        8.0              2.2   \n",
              "4           False       dimensity        8.0              2.6   \n",
              "\n",
              "   battery_capacity  fast_charging_available  fast_charging  ram_capacity  \\\n",
              "0            5000.0                        1          100.0          12.0   \n",
              "1            5000.0                        1           33.0           6.0   \n",
              "2            5000.0                        1           15.0           4.0   \n",
              "3            5000.0                        1            NaN           6.0   \n",
              "4            5000.0                        1           67.0           6.0   \n",
              "\n",
              "   internal_memory  screen_size  refresh_rate    resolution  num_rear_cameras  \\\n",
              "0            256.0         6.70           120  1440 x 3216                  3   \n",
              "1            128.0         6.59           120  1080 x 2412                  3   \n",
              "2             64.0         6.60            90  1080 x 2408                  3   \n",
              "3            128.0         6.55           120  1080 x 2400                  3   \n",
              "4            128.0         6.70           120  1080 x 2412                  3   \n",
              "\n",
              "   num_front_cameras       os  primary_camera_rear  primary_camera_front  \\\n",
              "0                1.0  android                 50.0                  16.0   \n",
              "1                1.0  android                 64.0                  16.0   \n",
              "2                1.0  android                 50.0                  13.0   \n",
              "3                1.0  android                 50.0                  16.0   \n",
              "4                1.0  android                108.0                  16.0   \n",
              "\n",
              "   extended_memory_available  extended_upto  \n",
              "0                          0            NaN  \n",
              "1                          1         1024.0  \n",
              "2                          1         1024.0  \n",
              "3                          1         1024.0  \n",
              "4                          0            NaN  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e56af6ac-e657-40a9-a034-a53cd3bfc414\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>brand_name</th>\n",
              "      <th>model</th>\n",
              "      <th>price</th>\n",
              "      <th>rating</th>\n",
              "      <th>has_5g</th>\n",
              "      <th>has_nfc</th>\n",
              "      <th>has_ir_blaster</th>\n",
              "      <th>processor_brand</th>\n",
              "      <th>num_cores</th>\n",
              "      <th>processor_speed</th>\n",
              "      <th>battery_capacity</th>\n",
              "      <th>fast_charging_available</th>\n",
              "      <th>fast_charging</th>\n",
              "      <th>ram_capacity</th>\n",
              "      <th>internal_memory</th>\n",
              "      <th>screen_size</th>\n",
              "      <th>refresh_rate</th>\n",
              "      <th>resolution</th>\n",
              "      <th>num_rear_cameras</th>\n",
              "      <th>num_front_cameras</th>\n",
              "      <th>os</th>\n",
              "      <th>primary_camera_rear</th>\n",
              "      <th>primary_camera_front</th>\n",
              "      <th>extended_memory_available</th>\n",
              "      <th>extended_upto</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>oneplus</td>\n",
              "      <td>OnePlus 11 5G</td>\n",
              "      <td>54999</td>\n",
              "      <td>89.0</td>\n",
              "      <td>True</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>snapdragon</td>\n",
              "      <td>8.0</td>\n",
              "      <td>3.2</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>100.0</td>\n",
              "      <td>12.0</td>\n",
              "      <td>256.0</td>\n",
              "      <td>6.70</td>\n",
              "      <td>120</td>\n",
              "      <td>1440 x 3216</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>50.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>oneplus</td>\n",
              "      <td>OnePlus Nord CE 2 Lite 5G</td>\n",
              "      <td>19989</td>\n",
              "      <td>81.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>snapdragon</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.2</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>33.0</td>\n",
              "      <td>6.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>6.59</td>\n",
              "      <td>120</td>\n",
              "      <td>1080 x 2412</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>64.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1024.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>samsung</td>\n",
              "      <td>Samsung Galaxy A14 5G</td>\n",
              "      <td>16499</td>\n",
              "      <td>75.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>exynos</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.4</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>15.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>64.0</td>\n",
              "      <td>6.60</td>\n",
              "      <td>90</td>\n",
              "      <td>1080 x 2408</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>50.0</td>\n",
              "      <td>13.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1024.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>motorola</td>\n",
              "      <td>Motorola Moto G62 5G</td>\n",
              "      <td>14999</td>\n",
              "      <td>81.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>snapdragon</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.2</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "      <td>6.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>6.55</td>\n",
              "      <td>120</td>\n",
              "      <td>1080 x 2400</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>50.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1024.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>realme</td>\n",
              "      <td>Realme 10 Pro Plus</td>\n",
              "      <td>24999</td>\n",
              "      <td>82.0</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>dimensity</td>\n",
              "      <td>8.0</td>\n",
              "      <td>2.6</td>\n",
              "      <td>5000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>67.0</td>\n",
              "      <td>6.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>6.70</td>\n",
              "      <td>120</td>\n",
              "      <td>1080 x 2412</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>android</td>\n",
              "      <td>108.0</td>\n",
              "      <td>16.0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e56af6ac-e657-40a9-a034-a53cd3bfc414')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e56af6ac-e657-40a9-a034-a53cd3bfc414 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e56af6ac-e657-40a9-a034-a53cd3bfc414');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# brand_name"
      ],
      "metadata": {
        "id": "y8qSOTD26eLB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# plot a graph of top 5 brands\n",
        "df['brand_name'].value_counts().head(10).plot(kind='bar')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 321
        },
        "id": "TlFM_1ZU6vTP",
        "outputId": "6104aa44-ad7e-41d0-a3e4-46e24e40006f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fb9a0284ca0>"
            ]
          },
          "metadata": {},
          "execution_count": 17
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAEfCAYAAAC6Z4bJAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAcSUlEQVR4nO3deZxldX3m8c8jq4AKSIlIA92aVoMLEQtBYRIVY3CIgguIChLFaROJohgNmmFaTBxRg4zLCLYgtpEgjZqAwY1hABcELRZZJXZYm4CUIojiBj7543cufSmqq7rq1v3dW6ee9+vVr6pzzr11vmLVc8/5nd8i20RERLs8bNAFRETE3Eu4R0S0UMI9IqKFEu4RES2UcI+IaKGEe0REC00b7pI+LekOSVdNcuztkixpm2Zbkj4qabWkKyTt2o+iIyJiautz5f4ZYJ+JOyXtALwQuLlr94uApc2/ZcAJvZcYEREzNW242/4mcOckh44H3gl0j4LaD/isi4uALSVtNyeVRkTEettwNm+StB9wq+0fSOo+tD1wS9f2mmbfbVP9vG222caLFy+eTSkREQvWJZdc8hPbI5Mdm3G4S9oMeDelSWbWJC2jNN2w4447MjY21suPi4hYcCTdtK5js+kt8wRgCfADSTcCi4BLJT0WuBXYoeu1i5p9D2F7he1R26MjI5N+8ERExCzNONxtX2n7MbYX215MaXrZ1fbtwFnAa5teM3sAd9ueskkmIiLm3vp0hTwN+C7wJElrJB02xcu/AlwPrAY+BbxpTqqMiIgZmbbN3farpjm+uOt7A4f3XlZERPQiI1QjIloo4R4R0UIJ94iIFkq4R0S00KxGqA7C4qPO7un9Nx677xxVEhEx/HLlHhHRQgn3iIgWmjfNMsOg16YhSPNQRNSRK/eIiBZKuEdEtFDCPSKihRLuEREtlHCPiGihhHtERAsl3CMiWijhHhHRQgn3iIgWSrhHRLRQwj0iooUS7hERLZRwj4hooYR7REQLTRvukj4t6Q5JV3Xt+5CkH0q6QtK/SNqy69i7JK2WdJ2kP+tX4RERsW7rc+X+GWCfCfvOAZ5q++nAvwPvApC0M3AQ8JTmPZ+QtMGcVRsREetl2nC3/U3gzgn7vmH7vmbzImBR8/1+wOdt/8b2DcBq4FlzWG9ERKyHuWhzfz3w1eb77YFbuo6tafZFRERFPYW7pL8D7gNOncV7l0kakzQ2Pj7eSxkRETHBrMNd0l8Afw68xrab3bcCO3S9bFGz7yFsr7A9ant0ZGRktmVERMQkZhXukvYB3gm8xPa9XYfOAg6StImkJcBS4Hu9lxkRETOx4XQvkHQa8FxgG0lrgOWU3jGbAOdIArjI9l/avlrSKuAaSnPN4bbv71fxERExuWnD3farJtl98hSvfx/wvl6KioiI3mSEakRECyXcIyJaKOEeEdFCCfeIiBZKuEdEtFDCPSKihRLuEREtlHCPiGihhHtERAtNO0I1hs/io87u6f03HrvvHFUSEcMqV+4RES2UcI+IaKGEe0RECyXcIyJaKOEeEdFCCfeIiBZKuEdEtFDCPSKihRLuEREtlHCPiGihhHtERAsl3CMiWmjacJf0aUl3SLqqa9/Wks6R9KPm61bNfkn6qKTVkq6QtGs/i4+IiMmtz5X7Z4B9Juw7CjjX9lLg3GYb4EXA0ubfMuCEuSkzIiJmYtpwt/1N4M4Ju/cDVjbfrwT279r/WRcXAVtK2m6uio2IiPUz2zb3bW3f1nx/O7Bt8/32wC1dr1vT7IuIiIp6fqBq24Bn+j5JyySNSRobHx/vtYyIiOgy23D/cae5pfl6R7P/VmCHrtctavY9hO0Vtkdtj46MjMyyjIiImMxsw/0s4NDm+0OBM7v2v7bpNbMHcHdX801ERFQy7Rqqkk4DngtsI2kNsBw4Flgl6TDgJuDA5uVfAf47sBq4F3hdH2qOiIhpTBvutl+1jkN7T/JaA4f3WlRERPRm2nCPmMzio87u+WfceOy+c1BJREwm0w9ERLRQwj0iooUS7hERLZRwj4hooYR7REQLJdwjIloo4R4R0UIJ94iIFkq4R0S0UMI9IqKFEu4RES2UcI+IaKFMHBbzViYvi1i3XLlHRLRQwj0iooUS7hERLZRwj4hooYR7REQLJdwjIloo4R4R0UIJ94iIFuop3CW9TdLVkq6SdJqkTSUtkXSxpNWSTpe08VwVGxER62fW4S5pe+AtwKjtpwIbAAcBHwCOt/0HwM+Aw+ai0IiIWH+9NstsCDxc0obAZsBtwPOBLzTHVwL793iOiIiYoVmHu+1bgX8EbqaE+t3AJcBdtu9rXrYG2L7XIiMiYmZ6aZbZCtgPWAI8Dtgc2GcG718maUzS2Pj4+GzLiIiISfTSLPMC4Abb47Z/B3wJ2BPYsmmmAVgE3DrZm22vsD1qe3RkZKSHMiIiYqJewv1mYA9Jm0kSsDdwDXAe8IrmNYcCZ/ZWYkREzFQvbe4XUx6cXgpc2fysFcDfAkdKWg08Gjh5DuqMiIgZ6GmxDtvLgeUTdl8PPKuXnxsREb3JCNWIiBZKuEdEtFDCPSKihRLuEREtlHCPiGihhHtERAsl3CMiWijhHhHRQgn3iIgWSrhHRLRQwj0iooUS7hERLZRwj4hooYR7REQLJdwjIloo4R4R0UIJ94iIFkq4R0S0UMI9IqKFEu4RES2UcI+IaKGEe0REC/UU7pK2lPQFST+UdK2kZ0vaWtI5kn7UfN1qroqNiIj10+uV+0eAr9l+MrALcC1wFHCu7aXAuc12RERUNOtwl/Qo4I+BkwFs/9b2XcB+wMrmZSuB/XstMiIiZqaXK/clwDhwiqTLJJ0kaXNgW9u3Na+5Hdi21yIjImJmegn3DYFdgRNsPwP4JROaYGwb8GRvlrRM0piksfHx8R7KiIiIiXoJ9zXAGtsXN9tfoIT9jyVtB9B8vWOyN9teYXvU9ujIyEgPZURExESzDnfbtwO3SHpSs2tv4BrgLODQZt+hwJk9VRgRETO2YY/vfzNwqqSNgeuB11E+MFZJOgy4CTiwx3NERMQM9RTuti8HRic5tHcvPzciInqTEaoRES2UcI+IaKGEe0RECyXcIyJaKOEeEdFCCfeIiBZKuEdEtFCvg5giFrzFR53d88+48dh956CSiLVy5R4R0UIJ94iIFkq4R0S0UMI9IqKFEu4RES2UcI+IaKGEe0RECyXcIyJaKIOYIlogA6lioly5R0S0UMI9IqKFEu4RES2UcI+IaKGEe0REC/Uc7pI2kHSZpH9rtpdIuljSakmnS9q49zIjImIm5qIr5BHAtcAjm+0PAMfb/rykE4HDgBPm4DwRMeTSJXN49BTukhYB+wLvA46UJOD5wKubl6wE3kPCPSIqyQdM0WuzzP8B3gn8vtl+NHCX7fua7TXA9j2eIyIiZmjW4S7pz4E7bF8yy/cvkzQmaWx8fHy2ZURExCR6uXLfE3iJpBuBz1OaYz4CbCmp09yzCLh1sjfbXmF71PboyMhID2VERMREsw532++yvcj2YuAg4P/bfg1wHvCK5mWHAmf2XGVERMxIP/q5/y3l4epqShv8yX04R0RETGFOZoW0fT5wfvP99cCz5uLnRkTE7GSEakRECyXcIyJaKOEeEdFCCfeIiBZKuEdEtFDWUI2I6INBz3GTK/eIiBZKuEdEtFDCPSKihRLuEREtlHCPiGihhHtERAsl3CMiWijhHhHRQgn3iIgWSrhHRLRQwj0iooUS7hERLZRwj4hooYR7REQLJdwjIloo4R4R0UKzDndJO0g6T9I1kq6WdESzf2tJ50j6UfN1q7krNyIi1kcvV+73AW+3vTOwB3C4pJ2Bo4BzbS8Fzm22IyKiolmHu+3bbF/afH8PcC2wPbAfsLJ52Upg/16LjIiImZmTNndJi4FnABcD29q+rTl0O7DtXJwjIiLWX8/hLmkL4IvAW23/vPuYbQNex/uWSRqTNDY+Pt5rGRER0aWncJe0ESXYT7X9pWb3jyVt1xzfDrhjsvfaXmF71PboyMhIL2VERMQEvfSWEXAycK3tD3cdOgs4tPn+UODM2ZcXERGzsWEP790TOAS4UtLlzb53A8cCqyQdBtwEHNhbiRERMVOzDnfb3wa0jsN7z/bnRkRE7zJCNSKihRLuEREtlHCPiGihhHtERAsl3CMiWijhHhHRQgn3iIgWSrhHRLRQwj0iooUS7hERLZRwj4hooYR7REQLJdwjIloo4R4R0UIJ94iIFkq4R0S0UMI9IqKFEu4RES2UcI+IaKGEe0RECyXcIyJaKOEeEdFCfQt3SftIuk7SaklH9es8ERHxUH0Jd0kbAP8XeBGwM/AqSTv341wREfFQ/bpyfxaw2vb1tn8LfB7Yr0/nioiICWR77n+o9ApgH9tvaLYPAXa3/dddr1kGLGs2nwRc1+NptwF+0uPP6NUw1ADDUccw1ADDUccw1ADDUccw1ADDUcdc1LCT7ZHJDmzY4w+eNdsrgBVz9fMkjdkenaufN19rGJY6hqGGYaljGGoYljqGoYZhqaPfNfSrWeZWYIeu7UXNvoiIqKBf4f59YKmkJZI2Bg4CzurTuSIiYoK+NMvYvk/SXwNfBzYAPm376n6cq8ucNfH0YBhqgOGoYxhqgOGoYxhqgOGoYxhqgOGoo6819OWBakREDFZGqEZEtFDCPSKihRLuEREtNLB+7jH3JG0BYPsXA6zh4cCOtnsdlBZzRNJmtu8ddB3DoOm998Rm8zrbv6t8/m2B3ZrN79m+o2/nmm8PVCUdbPtzko6c7LjtD1euZ7I67gYusX15pRqeBnwW2BoQMA4cavuqGufvquPFwD8CG9teIumPgPfafknFGhYBHwP2Agx8CzjC9ppaNXTVsi/wFGDTzj7b7614/ucAJwFb2N5R0i7AG22/qVYNTR0HAF+zfY+k/wnsCvyD7Usr1/FcYCVwI+XvZAfK38k3K53/QOBDwPnN+f8b8A7bX+jH+eZjs8zmzddHrONfbaPAXwLbN//eCOwDfErSOyvV8EngSNs72d4ReDuD6er1Hsq8QncBNB9uSyrXcAplTMV2wOOALzf7qpJ0IvBK4M2UP+QDgJ0ql3E88GfATwFs/wD448o1ABzdBPtewAuAk4ETBlDHccALbf+J7T+m/Lc5vuL5/w7Yzfahtl9L+Vs5ul8nm3fNMrY/2Xw9ZtC1NBYBu3aaQiQtB86m/BFdAnywQg2b2z6vs2H7fEmbT/WGPvmd7bslde+rfWs4Yrs7zD8j6a2VawB4ju2nS7rC9jGSjgO+WrsI27dM+P/j/to1dJ1zX2CF7bMl/cMA6tiou7nQ9r9L2qji+R82oRnmp/TxAnvehXuHpCWUq6LFdP3vqNkE0HgM8Juu7d8B29r+laTfrOM9c+16SUcD/9RsHwxcX+nc3a6W9GpgA0lLgbcAF1au4aeSDgZOa7ZfRXPlWtmvmq/3SnpcU8N2lWu4pWmacRNiRwDXVq4B4FZJnwT+FPiApE0YTKvBmKSTgM81268Bxiqe/2uSvs7a381XAl/p18nmXZt7h6QfUG7vrgR+39lv+4LKdRwNvBQ4s9n1YkqzwHGUq5TXVKhhK+AYSjszwDeBY2z/rN/nnlDHZpRbzxdSmiK+Dvy97V9XrGEnSpv7s5td3wHeYvvmWjU0dRzd1LE3ZW0DAyfZ7ttt+CQ1bAN8hNIUIuAblOcPVT/smt+LfYArbf9I0nbA02x/o3IdmwCHs/bv5FvAJ2zXughD0suBPTvnt/0vfTvXPA73i23vPug6ACTtBjyn2fyO7ZpXA0jatfbDqVh/TahsavvuQdcyCJJ2nGz/AD5wNwd+bfv+ZnsDYJO29iSaz+H+amAp5WrkgU/eQYRc80uyLQ9uHqr2iyvpPOCxwBeA02v3kumqYxR4Nw9tKnt6xRoeT7la3YNytfxd4G22qzRTSXrZVMdtf6lCDR9jimcdtt/S7xq6SbqSUo8oPYeWULohPqVyHRcBL+h6PrYF8A3bz5n6nXN2/pcBH6A05ar5Z9uP7Mf55m2bO/A04BDg+axtlnGzXY2kNwPLgR9THhypqaNaoNl+nqTHAgcCn5T0SErI135odSrwDiY0lVX2z5RmkJc22wdR2jhr3eW9eIpjBvoe7tRtR56W7ad1b0vaFajaHbOxafcYENu/aJqMavkg8GLbVZ57zOcr99XAzs0yfoOuY/fa7Zjr0vR5fyfwStsbVz73t23vNf0r+1rDFRPvFCT9wPYug6pp0JoPe9u+Z9C1dEi6cmLoVzjnd4A3d+7uJT0T+LjtZ0/9zrk7v+09p3/l3JjPV+5XAVsCfRvhtZ5uoQxaGhhJf0h58v5ySq+M0yl93Wtb3vRGOJcHN5XVuFrt+Kqkoyjr9pqmR4KkrZta7qxRhKRHUe7oOv3KL6AM6Kr2u9I0k51CGf8hSXcBr7d9Sa0amjq6B/o9jDKI6T9r1tB4K3CGpP+k3GE/lvL7UcuYpNOBf6XC38d8vnI/n9L08X0e/B+qaldISSdT1oA9e0Id1UbKSvouJdBX2R7EH02njs8BTwaupqupzPbrK9ZwwxSHbfvxler4IuUCZGWz6xBgF9tTtsnPcQ1XAIfb/lazvReld0i1JsPmvMu7Nu+jjBD9Ys1eVF21bET5e4XK0w9ImmwwXd/+PuZzuP/JZPsH0BVy+WT7h2iQVTWSrrP9pOlf2X6SLrf9R9Pt63MNl9l+xoR9l9retVYNw6QJ9r9i7d3U+cAna88vU8u8bZaxfUHNSXimqGNgIS5ple0Du3ojPHCIckVQ9QoNuFDSzravqXzeB0jalPKwrntumRMHcJX4K0l72f52U9eerB3YVMsFzeCh01jbRHV+80Cz7z3LJH2ZqXvt1B5weAKwEfCJZvuQZt8bapxc0krKOIO7mu2tgONy5T5B7Ul4pqjjPCb5Bbbd9147krazfZuktwMXAQ+aHMv2Tf2uYUI91wJPAG6gNFFV/5CRtAq4h7WjEF8NbGn7gFo1NHXsQpnM7VHNrp9RJqm6omIN501x2P3+HV3X3XVXAbXvsh/yYL3mw/Z13Ek9ZN9cmbdX7qydhOcOAEkjwP+j9PWu6W+6vt+U8lDzvhontn1b8+0WlInC7qS0vZ9h+8c1aphgnwGcc6Kn2t65a/s8SVXvJJpxD4fY3qXpqYLtn9esoTnn82qfc8L5Hwhvlal2n0y5ELpuQL3c7pf0BNv/0dT0eOrOtfMwSVt1Ro43D/n7lsHzOdyrTsKzLpP0PPiOpO9VruEY4BhJT6fcel8gaY3tF9Q4f6cnCuWKedAulbSH7YsAJO1O5X7ftu9vHl4OJNQ7JD2a0mOn00T1bUqPndrTD+wLnAj8B+VubomkN9quPZHaOygf9p0BbYuB11U8/3HAdyWd0WwfALyvXyebz+FedRKedekKNigfLs9k7a14bXcAt1M+6B5T8byXsHYE4kQGqvRQaTyT0vZ/c3PunYDrOs8lKjYRXSbpLOAM4JednZW7hX6eMs/Qy5vt11Du7Kp86Hc5Dnie7dUAkp5A6V1WO9y/Q5kee2/KtNRfp4xgrsL2ZyWNsXag5cv6+Xxq3ra5Q91JeKao4QbWBtt9lPbm93YepFWq4U2U0akjlDBZNciHmoOkMnHYVpRnMFDC7a7O8VrPIWp3e1tHDVfZfuqEfYMYPPR927t1bYvSAWK3Kd7WjzpWAT+njKSGATyPae7olto+pWlK3sL2VN13Z3+u+RzuUUh6P2W6gSorP01Ty1aUOX+6Vx+qstJNc/4jKL0fvkT5wN0f+JTtj9WqYVhI+jDwPWBVs+sVwLNs/82639WXOk6g3EGtolwIHQDcTHlGVu1uRtI1E57HTLqvj+dfTlnc50m2n6gyFfQZ/Rq1Om/DXdIelClV/xDYGNgA+KX7NAnPFHUMxRJiw0DSGyhzhi8CLqdM3vXdGj2Humq4Ani27V8225s3NdQeuNNZ7u+BO0sqL/cn6R7KymWdh4YbsLaJyLX+VtZxF9NR7W6mGWT38QnPYw53WRWpxvkvB54BXNrpIaNJpsuYK/O5zf3jlEmhzqB8Gr6WtQvf1nS07TO0dgmxD1H6zg7FdMSVHUEZd3CRy2RmTwb+d+UaxIN7QHQmc6vtFMokZp1b/oObfX9aqwDbj2ieCU28k6raBdF2zYeWU+l+HgOwI3Wfx/zWtiUZHrjw6Jv5HO7YXi1pA5f5mU+RdBnwrsplDMsSYsPg17Z/LQlJm9j+oaTaI1ZPAS6W1Hn+sj9lUZfaBr7c3zrupC6kPFCsWccTKRc829p+atOr6yWuP2vpoLvqrmoGlW0p6X8Arwc+1a+Tzedwv7fpO3u5pA8CtzGYpbuGZQmxYbBG0paUiZHOkfQzoOpAKtsfVpl3qDM75etsX1azhsYwLPc3DHdSUALsHZSeKti+QtI/A1XDvfagvkmMUMbh/Jwyv83/oo89l+Zzm/tOlK5/GwFvo3Q//ESnu1XFOoZiCbFh04xOfBTlecRAp2UeBD14uT9TrpjfbPuWijV83/ZuTVvv7rZ/I+lq118ko1PHA6MxVXmenWGgSeb1SZv7JLo+hX9FWT90UHXc2wzz3kHNnB3ATwZVz6BN0tVre0r30IVm0cS5U1Tml6kW7gzBnVTjJ03f9k5b8ysod9oLgqS/osx39PjmgX/HIyh97/tz3vl25a51T5YF1F3Srann74G/oIy+69TT93k7hlHtrl7DbB1XaQObkXGQd1LNMP8VlHWGf0b5sD/Y9o016xgUlbn9twLeDxzVdege93F9gfkY7p3Jsp4C/GLC4edPeIhVo57rKM0wC67pYaLaXb2GkaRnU0LsrcDxXYceCby01iRVw6jpHfIwD9GKUG0275pluibLOp0y696HKN28Pki5aqwa7gzPilDDoGpXryG1MWUitw0pt90dP6cMIlpwmk4GL6dZOL0MUAXb7x1gWa0378K9y+6UlcQvpPwRncraASM1vZ8yj8hVDHBFqEFrhpT/W82uXsOo6UN+gaTP2L5J0hbN/ol3mQvJmZSlKC+h628k+ms+h/vvKA9TH065cr/B9u+nfktfrKR8yFzJ2qXlFpzmiv0A4Ei6unrZPmewlQ3MI5pxF1sDSPoJZT73qwZb1kAssj3oPuYLznwO9+9Trgh2A7YBTpT08pqTADXutf3RyuccVpcCd9l+x6ALGQIrgCNtnwcg6bmsfai40Fwo6Wm2rxx0IQvJvHug2iFp1PbYhH2H2P6nynV8mHKreRYPbpZZiHPL/BD4A0p3u+5pbhfMA9UODXjVn2GisljKUuB6BrRC10I0b8N9WGjypcwWalfInSbbPwQjA6trpj+4FOhcbBwMPNP2SwdX1WBoHdMwL8Tfi5oS7hF90Ex9fAwPnhXyPW4WR15IMg3zYCTc54DKMmJP4cEz76Wb1wImaZSyzu9i1j7bWpBNEcMyDfNCM58fqA4FSScCmwHPA06i9GWuuoZqDKVTKYunX8UC7kXVGJZpmBeUhHvvnmP76c1IzGMkHUf9tSFj+Izb/vKgixgSwzIN84KScO/dr5uv9zZzqdwJbDfAemI4LJd0EnAuD+5FVXOB7KEwRNMwLygJ9959uZl570OU3hFmgY3KjEm9DngyZUrqTrOMKQ8VF5yma/CC6x48SAn33v0QuN/2FyXtTFlD9V8HXFMM3m62a69CFfGAhbpi0Fw6ulkcey/g+ZSHqicMuKYYvAubD/uIgUi49657DdVP2T6bMjNgLGx7UJaAvE7SFZKunLBQQ0RfpVmmd1lDNSaTibJioDKIqUdZQzUihlHCPSKihdJ8EBHRQgn3iIgWSrhHRLRQwj0iooUS7hERLfRf/reuo1s6EU8AAAAASUVORK5CYII=\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# pie chart\n",
        "df['brand_name'].value_counts().plot(kind='pie',autopct='%0.1f%%')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "zBuhav2H6yDh",
        "outputId": "f536640e-5e8e-4d6d-c71a-4da821e26ab2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fb9a01e57c0>"
            ]
          },
          "metadata": {},
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['brand_name'].isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PnyFi1TC7MzW",
        "outputId": "0ebb8896-8158-45a4-eb2b-d738ab88afcb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# model\n",
        "df['model'].nunique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tkEt7deZ7bYb",
        "outputId": "cc034ea1-5c33-4032-81e8-22af9163dfad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "980"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# price\n",
        "df['price'].describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y7Pd4CIA7in_",
        "outputId": "223e3592-e2f2-4be0-a54d-9b7030c9a920"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count       980.000000\n",
              "mean      32520.504082\n",
              "std       39531.812669\n",
              "min        3499.000000\n",
              "25%       12999.000000\n",
              "50%       19994.500000\n",
              "75%       35491.500000\n",
              "max      650000.000000\n",
              "Name: price, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.displot(kind='hist',data=df,x='price',kde=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 386
        },
        "id": "kVgFBf6a8APc",
        "outputId": "d9c65304-1ebe-4f86-d61f-867b657a33fe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x7fb9a01fbb50>"
            ]
          },
          "metadata": {},
          "execution_count": 24
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 360x360 with 1 Axes>"]
          }
        }
      ]
    }