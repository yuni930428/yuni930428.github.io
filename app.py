from flask import Flask, render_template, request
import random

app = Flask(__name__, static_folder='static')

# 更新的飲食計劃建議（包括圖片名稱）
diet_plans = {
    "weight_loss": [
        {"name": "低卡蔬菜沙拉", "image": "田園沙拉.jpg.webp"},
        {"name": "藜麥沙拉", "image": "藜麥沙拉.JPG"},
        {"name": "酪梨沙拉", "image": "酪梨沙拉.jpg"},
        {"name": "無米壽司", "image": "無米壽司.jpg"},
        {"name": "水果沙拉", "image": "水果沙拉.jpg"}
    ],
    "muscle_gain": [
        {"name": "高蛋白雞胸肉", "image": "#179 水煮雞胸肉.jpg"},
        {"name": "煎鮭魚", "image": " -26.jpg"},
        {"name": "蛋白質奶昔", "image": "高蛋白咖啡香蕉奶昔 (全素) Protein Banana Coffee Smoothie - Barrel Leaf 桶子葉.jpg"},
        {"name": "牛排", "image": "Seared Strip Steak + Baby Broccoli | Hungryroot.jpg"},
        {"name": "雞蛋料理", "image": "早餐食譜,便當食譜-豐富蔬菜烘烤玉子燒 | MASAの料理ABC.jpg"}
    ],
    "balanced": [
        {"name": "全麥三明治", "image": "伊莉的店 全麥三明治.jpg"},
        {"name": "鮭魚蔬菜湯", "image": "鮭魚頭豆腐湯 by happeabites.jpg"},
        {"name": "義大利麵", "image": "義大利海鮮冷麵【HOLA幸福食堂】－男人廚房1+1｜痞客邦.jpg"},
        {"name": "櫛瓜煎餅", "image": "夏南瓜(櫛瓜)煎餅.jpg"},
        {"name": "全麥麵包", "image": "現磨麵粉～全麥核桃蔓越莓歐包.jpg"}
    ],
    "maintain_weight": [
        {"name": "雞肉蔬菜沙拉", "image": "味增雞肉蔬菜沙拉.jpg"},
        {"name": "海鮮配蔬菜", "image": "Dinner Recipe.jpg"},
        {"name": "燕麥粥", "image": "Apple Cinnamon Buckwheat Porridge [Vegan].jpg"},
        {"name": "蒸魚配青菜", "image": "蒸魚配青菜.jpg"}
    ]
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_diet', methods=['POST'])
def get_diet():
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    goal = request.form['goal']
    preference = request.form['preference']

    # 基本的健康狀況分析（BMI 計算）
    bmi = weight / (height / 100) ** 2

    # 健康狀況分析，根據 BMI 值給出健康狀況
    if bmi < 18.5:
        health_status = "體重過輕"
    elif 18.5 <= bmi < 24.9:
        health_status = "正常範圍"
    elif 25 <= bmi < 29.9:
        health_status = "過重"
    else:
        health_status = "肥胖"

    # 根據目標選擇飲食計劃
    if goal == "weight_loss":
        diet_suggestion = diet_plans['weight_loss']
    elif goal == "muscle_gain":
        diet_suggestion = diet_plans['muscle_gain']
    elif goal == "maintain_weight":
        diet_suggestion = diet_plans['maintain_weight']
    else:
        diet_suggestion = diet_plans['balanced']

    # 如果偏好是素食，則過濾掉含肉類的選項
    if preference == "vegetarian":
        diet_suggestion = [item for item in diet_suggestion if "肉" not in item['name']]

    # 隨機選擇一個飲食建議
    selected_diet = random.choice(diet_suggestion)

    return render_template('result.html', selected_diet=selected_diet, bmi=bmi, health_status=health_status)

@app.route('/result')
def result():
    # 假設這是你從表單中取得的動態數據
    selected_diet = {"name": "低卡蔬菜沙拉", "image": "田園沙拉.jpg.webp"}
    bmi = 23.5
    health_status = "正常範圍"
    return render_template('result.html', selected_diet=selected_diet, bmi=bmi, health_status=health_status)


if __name__ == '__main__':
    app.run(debug=True)


