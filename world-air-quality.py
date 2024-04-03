import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import json



DATA = 'data/world_air_quality.csv'
convert_ISO_3166_2_to_1 = {
'AF':'AFG',
'AX':'ALA',
'AL':'ALB',
'DZ':'DZA',
'AS':'ASM',
'AD':'AND',
'AO':'AGO',
'AI':'AIA',
'AQ':'ATA',
'AG':'ATG',
'AR':'ARG',
'AM':'ARM',
'AW':'ABW',
'AU':'AUS',
'AT':'AUT',
'AZ':'AZE',
'BS':'BHS',
'BH':'BHR',
'BD':'BGD',
'BB':'BRB',
'BY':'BLR',
'BE':'BEL',
'BZ':'BLZ',
'BJ':'BEN',
'BM':'BMU',
'BT':'BTN',
'BO':'BOL',
'BA':'BIH',
'BW':'BWA',
'BV':'BVT',
'BR':'BRA',
'IO':'IOT',
'BN':'BRN',
'BG':'BGR',
'BF':'BFA',
'BI':'BDI',
'KH':'KHM',
'CM':'CMR',
'CA':'CAN',
'CV':'CPV',
'KY':'CYM',
'CF':'CAF',
'TD':'TCD',
'CL':'CHL',
'CN':'CHN',
'CX':'CXR',
'CC':'CCK',
'CO':'COL',
'KM':'COM',
'CG':'COG',
'CD':'COD',
'CK':'COK',
'CR':'CRI',
'CI':'CIV',
'HR':'HRV',
'CU':'CUB',
'CY':'CYP',
'CZ':'CZE',
'DK':'DNK',
'DJ':'DJI',
'DM':'DMA',
'DO':'DOM',
'EC':'ECU',
'EG':'EGY',
'SV':'SLV',
'GQ':'GNQ',
'ER':'ERI',
'EE':'EST',
'ET':'ETH',
'FK':'FLK',
'FO':'FRO',
'FJ':'FJI',
'FI':'FIN',
'FR':'FRA',
'GF':'GUF',
'PF':'PYF',
'TF':'ATF',
'GA':'GAB',
'GM':'GMB',
'GE':'GEO',
'DE':'DEU',
'GH':'GHA',
'GI':'GIB',
'GR':'GRC',
'GL':'GRL',
'GD':'GRD',
'GP':'GLP',
'GU':'GUM',
'GT':'GTM',
'GG':'GGY',
'GN':'GIN',
'GW':'GNB',
'GY':'GUY',
'HT':'HTI',
'HM':'HMD',
'VA':'VAT',
'HN':'HND',
'HK':'HKG',
'HU':'HUN',
'IS':'ISL',
'IN':'IND',
'ID':'IDN',
'IR':'IRN',
'IQ':'IRQ',
'IE':'IRL',
'IM':'IMN',
'IL':'ISR',
'IT':'ITA',
'JM':'JAM',
'JP':'JPN',
'JE':'JEY',
'JO':'JOR',
'KZ':'KAZ',
'KE':'KEN',
'KI':'KIR',
'KP':'PRK',
'KR':'KOR',
'KW':'KWT',
'KG':'KGZ',
'LA':'LAO',
'LV':'LVA',
'LB':'LBN',
'LS':'LSO',
'LR':'LBR',
'LY':'LBY',
'LI':'LIE',
'LT':'LTU',
'LU':'LUX',
'MO':'MAC',
'MK':'MKD',
'MG':'MDG',
'MW':'MWI',
'MY':'MYS',
'MV':'MDV',
'ML':'MLI',
'MT':'MLT',
'MH':'MHL',
'MQ':'MTQ',
'MR':'MRT',
'MU':'MUS',
'YT':'MYT',
'MX':'MEX',
'FM':'FSM',
'MD':'MDA',
'MC':'MCO',
'MN':'MNG',
'ME':'MNE',
'MS':'MSR',
'MA':'MAR',
'MZ':'MOZ',
'MM':'MMR',
'NA':'NAM',
'NR':'NRU',
'NP':'NPL',
'NL':'NLD',
'AN':'ANT',
'NC':'NCL',
'NZ':'NZL',
'NI':'NIC',
'NE':'NER',
'NG':'NGA',
'NU':'NIU',
'NF':'NFK',
'MP':'MNP',
'NO':'NOR',
'OM':'OMN',
'PK':'PAK',
'PW':'PLW',
'PS':'PSE',
'PA':'PAN',
'PG':'PNG',
'PY':'PRY',
'PE':'PER',
'PH':'PHL',
'PN':'PCN',
'PL':'POL',
'PT':'PRT',
'PR':'PRI',
'QA':'QAT',
'RE':'REU',
'RO':'ROU',
'RU':'RUS',
'RW':'RWA',
'BL':'BLM',
'SH':'SHN',
'KN':'KNA',
'LC':'LCA',
'MF':'MAF',
'PM':'SPM',
'VC':'VCT',
'WS':'WSM',
'SM':'SMR',
'ST':'STP',
'SA':'SAU',
'SN':'SEN',
'RS':'SRB',
'SC':'SYC',
'SL':'SLE',
'SG':'SGP',
'SK':'SVK',
'SI':'SVN',
'SB':'SLB',
'SO':'SOM',
'ZA':'ZAF',
'GS':'SGS',
'ES':'ESP',
'LK':'LKA',
'SD':'SDN',
'SR':'SUR',
'SJ':'SJM',
'SZ':'SWZ',
'SE':'SWE',
'CH':'CHE',
'SY':'SYR',
'TW':'TWN',
'TJ':'TJK',
'TZ':'TZA',
'TH':'THA',
'TL':'TLS',
'TG':'TGO',
'TK':'TKL',
'TO':'TON',
'TT':'TTO',
'TN':'TUN',
'TR':'TUR',
'TM':'TKM',
'TC':'TCA',
'TV':'TUV',
'UG':'UGA',
'UA':'UKR',
'AE':'ARE',
'GB':'GBR',
'US':'USA',
'UM':'UMI',
'UY':'URY',
'UZ':'UZB',
'VU':'VUT',
'VE':'VEN',
'VN':'VNM',
'VG':'VGB',
'VI':'VIR',
'WF':'WLF',
'EH':'ESH',
'YE':'YEM',
'ZM':'ZMB',
'ZW':'ZWE'
}
@st.cache_data
def load_data():
    return pd.read_csv(DATA, delimiter=';')



#добавим статистики
def top_ten(substance, data, unit):
    pollution = data.loc[data["Pollutant"] == substance].sort_values(by= 'Value', ascending= False)
    pollution = pollution.loc[data["Unit"] == unit]
    pollution = pollution['Country Label'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=pollution[:10].index, y=pollution[:10], palette='viridis', ax=ax)
    plt.xticks(rotation=90)
    plt.grid(color="black", linestyle='--', axis='y')
    plt.title(f"Top 10 countries with the most polluted locations by {substance} in {unit}")
    return fig


#отображаем на карте страны, загрязненные определенным веществом
def plot_map(substance,data, unit):
    sub_countries = data.loc[data['Pollutant'] == substance]
    sub_countries = sub_countries.loc[sub_countries['Unit'] == unit]
    sub_countries = sub_countries.groupby('Country Code')['Value'].mean()
    sub_countries =  pd.DataFrame(sub_countries)
    sub_countries = sub_countries.reset_index()
    fig = px.choropleth_mapbox(
        sub_countries,
        locations="Country Code", 
        geojson= json_locations,
        color='Value', 
        hover_name="Country Code", 
        hover_data=['Value'], 
        color_continuous_scale='BuGn',
        opacity= 1,
        zoom=0,
        mapbox_style='carto-positron'
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},coloraxis_colorbar=dict(title=unit))

    return fig


data = load_data()

#переводим коды в alpha-1
data["Country Code"] = data['Country Code'].replace(convert_ISO_3166_2_to_1)

#чистим данные от значений меньше нуля
data = data.drop(data[data['Value']<0].index)

# чистим данные от единиц измерения с маленьким количеством
data = data.drop(data[data['Unit'] == 'c'].index)
data = data.drop(data[data['Unit'] == '%'].index)
data = data.drop(data[data['Unit'] == 'particles/cm³'].index)

#чистим данные от загрязнителя с маленьким количеством
for pol in ['BC','PM1', 'TEMPERATURE', 'RELATIVEHUMIDITY', 'UM003']:     
    data = data.drop(data[data['Pollutant'] == pol].index)

with open('data/countries.geo.json') as json_file:
    json_locations = json.load(json_file)


#ЗАГОЛОВКИ
#для страницы
st.title("Качество воздуха в мире")
st.write("""Данный дашборд показывает качество воздуха во всем мире по странам (наличие в воздухе 
         определенных веществ)""")

#sidebar
st.sidebar.title("Выбор загрязнителя")

#st.dataframe(data)

#SIDEBAR
substance = st.sidebar.selectbox(
    'Выберите "загрязнитель"',
    ('NO', 'NO2', 'NOX', 'SO2', 'PM2.5', 'CO', 'O3', 'PM10')
)
unit = st.sidebar.radio(
    "Выбрать единицы измерения",
    ['ppm', 'µg/m³']
)
map = st.sidebar.checkbox("Отобразить на карте")
chart = st.sidebar.checkbox("Вывести график")

if map:
    
    st.plotly_chart(plot_map(substance, data,unit))

if chart:
    st.pyplot(top_ten(substance, data,unit))
#fig.show()
#отображение карты
#st.plotly_chart()
#отобрадение графиков
#st.pyplot(top_ten('NO', data))