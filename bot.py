<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Salman OSINT | لوحة القيادة السيبرانية</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Courier New', Courier, monospace;
        }
        body {
            background-color: #03030c;
            color: #00ff66;
            overflow-x: hidden;
            background-image: 
                radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
                radial-gradient(white, rgba(255,255,255,.1) 1px, transparent 30px);
            background-size: 550px 550px, 350px 350px;
            background-position: 0 0, 40px 60px;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background: rgba(0, 0, 0, 0.8);
            border-bottom: 2px solid #00ff66;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #00ff66;
            text-shadow: 0 0 10px #00ff66;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin-left: 20px;
            padding: 8px 15px;
            border: 1px solid #00ff66;
            transition: 0.3s;
            background: rgba(0, 255, 102, 0.1);
        }
        nav a:hover {
            background: #00ff66;
            color: #000;
            box-shadow: 0 0 15px #00ff66;
        }
        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
        }
        .card {
            background: rgba(10, 10, 25, 0.9);
            border: 1px solid #00ff66;
            padding: 20px;
            border-radius: 5px;
            box-shadow: inset 0 0 10px rgba(0, 255, 102, 0.2);
            margin-bottom: 20px;
        }
        h2 {
            border-bottom: 1px dashed #00ff66;
            padding-bottom: 10px;
            margin-bottom: 15px;
            font-size: 18px;
            color: #fff;
        }
        .terminal-line {
            margin: 8px 0;
            color: #00ff66;
        }
        .cmd-badge {
            background: #00ff66;
            color: #000;
            padding: 2px 6px;
            font-weight: bold;
            font-size: 12px;
            margin-left: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        th, td {
            border: 1px solid #00ff66;
            padding: 10px;
            text-align: center;
        }
        th {
            background: rgba(0, 255, 102, 0.2);
        }
        .rank-1 {
            background: rgba(255, 215, 0, 0.2);
            color: #ffd700;
            font-weight: bold;
        }
        .map-box {
            width: 100%;
            height: 250px;
            background: linear-gradient(45deg, #020024, #090979, #00d4ff);
            border: 1px solid #00ff66;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        .pulse-dot {
            width: 15px;
            height: 15px;
            background: #ff0055;
            border-radius: 50%;
            box-shadow: 0 0 0 0 rgba(255, 0, 85, 0.7);
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 85, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 15px rgba(255, 0, 85, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 85, 0); }
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">[ سلمان العنزي - OSINT COMMAND CENTER ]</div>
        <nav>
            <a href="#dashboard">الرئيسية</a>
            <a href="security-analysis.html" id="security-btn">الامان (تحليل شامل)</a>
            <a href="#tools">الأدوات</a>
            <a href="#live-map">خريطة البث</a>
        </nav>
    </header>

    <div class="container">
        <div class="grid">
            <!-- التيرمينال والأدوات -->
            <div>
                <div class="card" id="tools">
                    <h2>أدوات التحليل المضافة حديثاً</h2>
                    <div class="terminal-line">> WhatsMyName <span class="cmd-badge">salmaan go</span></div>
                    <div class="terminal-line">> Google Dorks <span class="cmd-badge">salmaan go</span></div>
                    <div class="terminal-line">> OSINT Industries <span class="cmd-badge">salmaan go</span></div>
                </div>

                <div class="card" id="live-map">
                    <h2>خريطة البث المباشر الملونة (تتبع الأهداف)</h2>
                    <div class="map-box">
                        <div style="position: absolute; top: 15px; right: 15px; color: #fff; font-size: 12px;">LIVE FEED - RIYADH SECTOR</div>
                        <div class="pulse-dot"></div>
                    </div>
                </div>
            </div>

            <!-- لوحة الصدارة -->
            <div>
                <div class="card">
                    <h2>لوحة التصنيف (Global Rank)</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>المركز</th>
                                <th>المستخدم / الفريق</th>
                                <th>النقاط</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="rank-1">
                                <td>1</td>
                                <td>سلمان العنزي (Salman Alanzi KSA)</td>
                                <td>9999</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>Cyber_Ghost</td>
                                <td>8450</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td>RootX_9</td>
                                <td>7920</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('security-btn').addEventListener('click', function(e) {
            e.preventDefault();
            window.location.href = "security-analysis.html";
        });
    </script>
</body>
</html>
