import streamlit as st
from random import randint, sample
from sortingAlgo import run_insertion_sort, run_selection_sort, run_quick_sort, run_merge_sort
from helper import chartRunTime, AVG, WORST, BEST
import pandas as pd
import altair as alt

INSERTION_SORT = "Insertion"
SELECTION_SORT = "Selection"
MERGE_SORT="Merge"
QUICK_SORT="Quick"

st.set_page_config(
    page_title="Mr.Time Complexity",
    page_icon=":rocket:",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title(":alarm_clock: Complexity Checker")

if 'arr' not in st.session_state:
    st.session_state.arr = [randint(-49999, 49990) for _ in range(35000)]

if 'step' not in st.session_state:
    st.session_state.step = [10, 100, 500, 750, 1000, 2000, 5000, 8000, 10000, 15000, 20000, 25000, 30000, 35000]

if 'idx' not in st.session_state:
    st.session_state.idx = None

if 'algo' not in st.session_state:
    st.session_state.algo = None

def format_func(opt):
    return st.session_state.step[opt]

with st.sidebar:
    st.header(":gear: Configuration")

    with st.form("config-form"):
        algo = st.selectbox("Sorting Algorithm", options=[INSERTION_SORT,
                                                          SELECTION_SORT,
                                                          MERGE_SORT,
                                                          QUICK_SORT],
                    index=None, placeholder="pick an algorithm")
        arr_size = st.select_slider("Array size", options=list(range(len(st.session_state.step))),
                                    format_func=format_func)

        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if algo == INSERTION_SORT:
                st.session_state.algo=run_insertion_sort
            elif algo == SELECTION_SORT:
                st.session_state.algo = run_selection_sort
            elif algo == MERGE_SORT:
                st.session_state.algo = run_merge_sort
            elif algo == QUICK_SORT:
                st.session_state.algo = run_quick_sort
            else:
                st.error("Pick a value")
            
            st.session_state.idx = arr_size

button = st.button(":arrow_forward: Run")
if button:
    if st.session_state.algo is None:
        st.error("Please Pick an Algorithm to continue")
    else:
        with st.spinner("Running Algorithm..."):
            timePlot = chartRunTime(st.session_state.arr,
                                    st.session_state.algo,
                                    [st.session_state.step[i] for i in range(0, st.session_state.idx + 1)])
            
            df = pd.DataFrame.from_dict(timePlot, orient='index')
            # df = pd.DataFrame([{'n': k, 'Time (ms)': v} for k, v in timePlot.items()])
        
       
        st.dataframe(df)
        # 2) build DataFrame with 'n' as a column
        df = (
            pd.DataFrame.from_dict(timePlot, orient='index')  # rows=cases, cols=n
            .T                                          # now rows=n, cols=cases
            .reset_index()
            .rename(columns={'index':'n'})
        )

        # 3) melt to long form
        df_long = df.melt(
            id_vars='n',
            value_vars=[BEST, WORST, AVG],
            var_name='case',
            value_name='time_ms'
        )


        # 4) Altair chart with manual colors
        color_scale = alt.Scale(
            domain=[BEST, WORST, AVG],
            range=['green','red','blue']
        )

        chart = (
            alt.Chart(df_long)
            .mark_line(point=True)
            .encode(
                x=alt.X('n:Q', title='Input size (n)'),
                y=alt.Y('time_ms:Q', title='Time (ms)'),
                color=alt.Color('case:N', scale=color_scale, legend=alt.Legend(title="Case"))
            )
            .properties(width=700, height=400)
        )

        # 5) render
        st.altair_chart(chart, use_container_width=True)