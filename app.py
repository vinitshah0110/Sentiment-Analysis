<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
  <title>Twitter Sentiment Analysis</title>

  <!-- CSS  -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="./static/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  <link href="./static/css2/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
</head>

<body>

  <div class="section no-pad-bot" id="index-banner">
    <div class="container">
      <br><br>
      <h1 class="header center orange-text">Twitter Sentiment Analysis</h1>
      <div class="row center">
        <h5 class="header col s12 light">Classify the sentiment into positive, negative and neutral.
        <br>
        </h5>
      </div>

              <div class="row">
    <form action='/predict' method="post" class="col s12">
      <div class="row">
        <div class="input-field col s4">
            <label for="first_name"><b>Twitter Text</b></label>
            <br>
          <input placeholder="Twitter Cleaned Data" name="Temperature" id="first_name" type="text" class="validate">
        </div>

      </div>

      <div class="row center">

          <button type="submit" class="btn-large waves-effect waves-light orange">Find Sentiment</button>
      </div>
    </form>
      </div>

      <br>
        {{pred}}<br>

    </div>
  </div>


    <br><br>
  </div>
  </div>>


  </body>
</html>
