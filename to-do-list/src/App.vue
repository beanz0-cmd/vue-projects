<script setup>
import Main from "@/components/Main.vue";
const href = "https://vuejs.org/";
const target = "_blank";
</script>

<template>
    <div class="Header">
        <h1>To-Do List</h1>
    </div>
    <Main />

    <div class="Footer">
        <p>
            This to-do-list was forged in the hellfires of
            <a :href="href" :target="target">vue.js</a>
        </p>
    </div>
</template>

<style scoped>
* {
    box-sizing: border-box;
    font-family: "Inter", sans-serif;
}

h1 {
    font-weight: 700;
}

.Header {
    height: 80px;
    width: 100%;
    text-align: center;
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1;
    background-color: white;
}

a {
    text-decoration: none;
    color: black;
}

a:hover {
    text-decoration: underline;
    color: #d01c1f;
}

.Footer {
    height: 100px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    bottom: 0;
    right: 0;
    z-index: 1;
    background-color: white;
}
</style>
