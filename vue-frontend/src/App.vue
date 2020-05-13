<template>
  <v-app>
    <v-content>
      <FileUpload />
      <TextInput />
    </v-content>
  </v-app>
</template>

<script>
import FileUpload from "@/components/FileUpload";
import TextInput from "@/components/TextInput";

export default {
  name: "App",
  components: {
    FileUpload,
    TextInput
  }
};
</script>
