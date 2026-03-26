<script setup>
import { ref, computed } from "vue";
const error = ref("");
const showErr = ref(false);
const myTodo = ref("");
const array = ref([]);

function handleSubmit() {
    if (!myTodo.value.trim()) {
        error.value = "Error: Input cannot be empty.";
        showErr.value = true;
        return;
    }
    addToArray();
}

function addToArray() {
    array.value.push({ id: Date.now(), text: myTodo.value, done: false });
    myTodo.value = "";
    error.value = "";
    showErr.value = false;
}

function deleteElement(id) {
    const item = array.value.find((item) => item.id === id);
    if (!item.done) {
        error.value = " Error: Todo is unchecked...";
        showErr.value = true;
    } else {
        error.value = "";
        showErr.value = false;
        array.value = array.value.filter((item) => item.id !== id);
    }
}

const total = computed(() => array.value.length);
const completed = computed(
    () => array.value.filter((item) => item.done).length,
);

function deleteAllChecked() {
    array.value = array.value.filter((item) => !item.done);
    error.value = "";
    showErr.value = false;
}
</script>

<template>
    <label v-if="showErr" id="lerror">{{ error }}</label>
    <div class="iContainer">
        <form @submit.prevent="handleSubmit">
            <input autofocus v-model="myTodo" placeholder="Add todo" />
            <button id="add" type="submit">Add</button>
        </form>
        <button id="rmAll" @click="deleteAllChecked">Remove All Checked</button>
        <p>Completed tasks {{ completed }}/{{ total }}</p>
    </div>
    <div class="lContainer">
        <ul>
            <li v-for="(item, index) in array" :key="item.id">
                <input
                    class="textInput"
                    type="checkbox"
                    :id="`todo-${index}`"
                    v-model="item.done"
                />
                <label :for="`todo-${index}`">{{ item.text }}</label>
                <button id="delete" @click="deleteElement(item.id)">🗑️</button>
            </li>
        </ul>
    </div>
</template>

<style scoped>
* {
    font-family: "Inter", sans-serif;
}

input,
button {
    font-weight: 400;
    background-color: white;
    border: 1px solid #666362;
    border-radius: 10px;
}

.iContainer {
    height: 100px;
    display: flex;
    align-items: baseline;
    justify-content: center;
    position: fixed;
    top: 75px;
    bottom: 0;
    right: 0;
    left: 0;
}

.lContainer {
    max-height: 550px;
    max-width: 100%;
    background-color: white;
    overflow-y: auto;
    position: fixed;
    top: 150px;
    bottom: 0;
    right: 0;
    left: 0;
    padding: 30px 0px 0px 50px;
}

ul {
    display: grid;
    grid-template-columns: auto auto auto;
}

li {
    list-style-type: none;
}

#lerror {
    color: white;
    background-color: #d01c1f;
    border: 2px solid darkred;
    border-radius: 15px;
    position: fixed;
    display: flex;
    justify-content: center;
    top: 130px;
    right: 0;
    left: 0;
    z-index: 2;
}

#add {
    margin: 20px 10px;
}

#rmAll {
    margin: 10px 10px 10px 0px;
}

#delete {
    margin: 10px 10px;
    background-color: white;
    border: 1px solid #666362;
    border-radius: 10px;
}

p {
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 50;
}
</style>
