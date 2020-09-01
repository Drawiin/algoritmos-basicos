/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula25;

import javax.swing.JOptionPane;

/**
 *
 * @author vini6
 */
public class Dialog01 extends javax.swing.JFrame {

    /**
     * Creates new form Dialog
     */
    public Dialog01() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        btnInfo = new javax.swing.JButton();
        btnAdvertencia = new javax.swing.JButton();
        btnQuestionamento = new javax.swing.JButton();
        btnErro = new javax.swing.JButton();
        btnMenssagem = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        btnInfo.setText("Informação");
        btnInfo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnInfoActionPerformed(evt);
            }
        });

        btnAdvertencia.setText("Advertencia");
        btnAdvertencia.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAdvertenciaActionPerformed(evt);
            }
        });

        btnQuestionamento.setText("Questionamento");
        btnQuestionamento.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnQuestionamentoActionPerformed(evt);
            }
        });

        btnErro.setText("Erro");
        btnErro.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnErroActionPerformed(evt);
            }
        });

        btnMenssagem.setText("Menssagem");
        btnMenssagem.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnMenssagemActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(155, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.CENTER)
                    .addComponent(btnInfo)
                    .addComponent(btnAdvertencia)
                    .addComponent(btnQuestionamento)
                    .addComponent(btnErro)
                    .addComponent(btnMenssagem))
                .addGap(133, 133, 133))
        );

        layout.linkSize(javax.swing.SwingConstants.HORIZONTAL, new java.awt.Component[] {btnAdvertencia, btnErro, btnInfo, btnMenssagem, btnQuestionamento});

        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(btnInfo)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnAdvertencia)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnErro)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnQuestionamento)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnMenssagem)
                .addContainerGap(114, Short.MAX_VALUE))
        );

        layout.linkSize(javax.swing.SwingConstants.VERTICAL, new java.awt.Component[] {btnAdvertencia, btnErro, btnInfo, btnMenssagem, btnQuestionamento});

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnInfoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnInfoActionPerformed
        // TODO add your handling code here:
        JOptionPane.showMessageDialog(null, "Informação", "Informação", JOptionPane.INFORMATION_MESSAGE);
    }//GEN-LAST:event_btnInfoActionPerformed

    private void btnAdvertenciaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAdvertenciaActionPerformed
        JOptionPane.showMessageDialog(null, "Advertencia", "Advertencia", JOptionPane.WARNING_MESSAGE);
    }//GEN-LAST:event_btnAdvertenciaActionPerformed

    private void btnErroActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnErroActionPerformed
        JOptionPane.showMessageDialog(null, "Erro", "Erro", JOptionPane.ERROR_MESSAGE);
    }//GEN-LAST:event_btnErroActionPerformed

    private void btnQuestionamentoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnQuestionamentoActionPerformed
        JOptionPane.showMessageDialog(null, "Questionamento", "Questionamento", JOptionPane.QUESTION_MESSAGE);
    }//GEN-LAST:event_btnQuestionamentoActionPerformed

    private void btnMenssagemActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnMenssagemActionPerformed
        JOptionPane.showMessageDialog(null, "Menssagem", "Menssagem", JOptionPane.PLAIN_MESSAGE);
    }//GEN-LAST:event_btnMenssagemActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Dialog01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Dialog01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Dialog01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Dialog01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Dialog01().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAdvertencia;
    private javax.swing.JButton btnErro;
    private javax.swing.JButton btnInfo;
    private javax.swing.JButton btnMenssagem;
    private javax.swing.JButton btnQuestionamento;
    // End of variables declaration//GEN-END:variables
}