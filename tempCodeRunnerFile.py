
        return render_template('signup.html')

@app.route('/FoodReccomendation' ,methods=["GET", "POST"])
@login_required